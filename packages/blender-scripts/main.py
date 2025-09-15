#!/usr/bin/env python3
"""
Blender headless entry.
Usage (outside Blender as stub):
  python main.py --job path/to/job.json
Within Blender:
  blender -b -P main.py -- --job path/to/job.json
If bpy is available, performs a minimal deterministic turntable render.
"""
import json, sys, os
# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import bpy  # type: ignore
except Exception:
    bpy = None

try:
    from .scene_setup import iso_camera_settings
    from . import import_assets
except ImportError:
    # Fallback for when run as script
    import scene_setup
    iso_camera_settings = scene_setup.iso_camera_settings
    import import_assets

def parse_args(argv):
    job = None
    i = 0
    while i < len(argv):
        if argv[i] == '--':
            i += 1
            break
        i += 1
    while i < len(argv):
        if argv[i] == '--job' and i+1 < len(argv):
            job = argv[i+1]
            i += 2
            continue
        i += 1
    return job

def load_job(job_path):
    with open(job_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_stub(job, out_dir):
    # Stub plan writer when not running inside Blender
    bonemap_info = None
    prof = job.get('retargetProfile')
    if prof:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        bm_path = os.path.join(base_dir, 'bonemaps', f"{prof}.json")
        if os.path.exists(bm_path):
            try:
                with open(bm_path, 'r', encoding='utf-8') as bf:
                    bonemap_info = json.load(bf)
            except Exception as e:
                bonemap_info = { 'error': str(e) }
    dirs = int(job.get('directions', 8) or 8)
    step = 360.0 / dirs
    directionAngles = [(i * step) % 360.0 for i in range(dirs)]
    cam = iso_camera_settings(job.get('projection', 'isometric'), job.get('camera', {}))
    plan = {
        'jobId': job.get('jobId'),
        'input': job.get('input'),
        'directions': dirs,
        'projection': job.get('projection', 'isometric'),
        'passes': job.get('passes', []),
        'status': 'planned',
        'notes': 'This is a stub response from blender-scripts/main.py',
        'retargetProfile': prof,
        'boneMapLoaded': bool(bonemap_info) and 'map' in bonemap_info,
        'boneMapSummary': { 'keys': list(bonemap_info.get('map', {}).keys())[:5] } if isinstance(bonemap_info, dict) else None,
        'directionAngles': directionAngles,
        'camera': cam,
        'lighting': job.get('lighting', {})
    }
    plan_path = os.path.join(out_dir, 'plan.json')
    with open(plan_path, 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2)
    print(f"Wrote {plan_path}")

def run_blender(job, out_dir):
    # Minimal deterministic scene and turntable render producing PNG frames.
    # This will render a placeholder cube if no assets are present.
    import math
    # Basic scene setup
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_EEVEE'
    scene.eevee.taa_render_samples = 1
    scene.eevee.use_bloom = False
    scene.eevee.use_ssr = False
    scene.use_nodes = False
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.resolution_x = int(job.get('resolution', 256))
    scene.render.resolution_y = int(job.get('resolution', 256))

    # Camera
    cam_data = bpy.data.cameras.new(name='SF_Camera')
    cam_data.type = 'ORTHO'
    cam = bpy.data.objects.new('SF_Camera', cam_data)
    bpy.context.collection.objects.link(cam)
    scene.camera = cam
    cam_cfg = job.get('camera', {})
    cam_data.ortho_scale = float(cam_cfg.get('orthoScale', 2.0))
    # Position camera with iso tilt
    tilt_deg = iso_camera_settings(job.get('projection', 'isometric'), cam_cfg)['tilt_deg']
    yaw_deg = iso_camera_settings(job.get('projection', 'isometric'), cam_cfg)['yaw_deg']
    # Place camera at fixed distance
    cam.location = (0.0, -5.0, 5.0)
    cam.rotation_euler = (
        math.radians(tilt_deg),
        0.0,
        math.radians(yaw_deg)
    )

    # Light
    light_data = bpy.data.lights.new(name='SF_Key', type='SUN')
    light_data.energy = 3.0
    light = bpy.data.objects.new(name='SF_Key', object_data=light_data)
    bpy.context.collection.objects.link(light)
    light.rotation_euler = (math.radians(45.0), 0.0, math.radians(35.0))

    # Subject: Try to import user rig else use a cube
    subject = None
    rig_path = job.get('rigSrcAbs')
    if rig_path and os.path.exists(rig_path):
        try:
            rig_info = import_assets.import_rig(rig_path)
            subject = rig_info.get('armature') or (rig_info.get('objects') or [None])[0]
        except Exception as e:
            print(f"Rig import failed: {e}")
            subject = None
    if subject is None:
        bpy.ops.mesh.primitive_cube_add(size=1)
        subject = bpy.context.active_object

    # Turntable angles
    dirs = int(job.get('directions', 8) or 8)
    step = 360.0 / dirs
    angles = [(i * step) % 360.0 for i in range(dirs)]

    # Clips from job
    clips = job.get('clips') or [{ 'name': 'preview', 'frames': 16, 'loop': True }]
    animClips = job.get('animClips') or []
    root_out = out_dir
    os.makedirs(root_out, exist_ok=True)

    for clip in clips:
        name = clip.get('name')
        frames = int(clip.get('frames') or 1)
        # Attempt to bind action if available
        action = None
        for acl in animClips:
            if acl.get('name') == name and os.path.exists(acl.get('src','')):
                try:
                    action = import_assets.import_animation_fbx(acl['src'])
                except Exception as e:
                    print(f"Anim import failed for {name}: {e}")
                break
        if subject and action:
            subject.animation_data_create()
            subject.animation_data.action = action
            scene.frame_start = 1
            scene.frame_end = max(1, int(frames))

        for d_i, yaw in enumerate(angles):
            # Rotate subject around Z for yaw
            subject.rotation_euler[2] = math.radians(yaw)
            # Render frames (placeholder: render same view per frame index)
            dir_dir = os.path.join(root_out, f"frames_{name}", f"dir_{d_i}")
            os.makedirs(dir_dir, exist_ok=True)
            for f in range(frames):
                scene.frame_set(f+1)
                scene.render.filepath = os.path.join(dir_dir, f"{f:04d}.png")
                bpy.ops.render.render(write_still=True)

    # Write a simple plan.json for parity
    plan = {
        'status': 'rendered',
        'clips': clips,
        'directions': dirs,
        'framesRoot': root_out,
    }
    plan_path = os.path.join(out_dir, 'plan.json')
    with open(plan_path, 'w', encoding='utf-8') as f:
        json.dump(plan, f, indent=2)
    print(f"Rendered frames to {root_out}")

def main():
    job_path = parse_args(sys.argv)
    if not job_path:
        print('Missing --job <file.json>')
        sys.exit(2)
    job = load_job(job_path)
    out_dir = job.get('output') or './dist'
    os.makedirs(out_dir, exist_ok=True)
    if bpy is None:
        run_stub(job, out_dir)
    else:
        run_blender(job, out_dir)

if __name__ == '__main__':
    main()
