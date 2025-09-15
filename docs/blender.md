# Blender Integration

Entry

- Run with Blender: `blender -b -P packages/blender-scripts/main.py -- --job dist/<name>/job.json`
- Or as stub (no bpy): `python3 packages/blender-scripts/main.py -- --job dist/<name>/job.json`

Job contract

- camera, lighting, directions, projection, resolution
- rigSrcAbs — absolute path to rig (FBX/GLB)
- animClips — [{ name, src (abs), frames, loop }]
- retargetProfile — e.g. mixamo_humanoid

Determinism

- Orthographic camera with fixed iso tilt/yaw
- Eevee with low/no TAA, bloom/SSR disabled
- Fixed PNG format, no timestamps (written by Blender)

Import

- `import_assets.import_rig(path)`: imports FBX/GLTF, returns created objects and armature
- `import_assets.import_animation_fbx(path)`: imports anim FBX and returns an Action
- For MVP, action bound directly to subject armature; retargeting to base rig TBD

Turntable

- Directions computed as 360/d, index 0 = North, clockwise
- Subject rotated on Z; camera fixed in iso orientation

Outputs

- Frames written to `frames_<clip>/dir_<d>/<frame>.png`
- plan.json summarizes clips/directions and frames root
