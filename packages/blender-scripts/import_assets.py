try:
    import bpy  # type: ignore
except Exception:
    bpy = None

def _with_bpy():
    if bpy is None:
        raise RuntimeError('bpy not available')

def import_fbx(filepath: str):
    _with_bpy()
    prev_objs = set(bpy.data.objects.keys())
    bpy.ops.import_scene.fbx(filepath=filepath, automatic_bone_orientation=True)
    new_objs = [bpy.data.objects[name] for name in bpy.data.objects.keys() if name not in prev_objs]
    arm = next((o for o in new_objs if o.type == 'ARMATURE'), None)
    return { 'objects': new_objs, 'armature': arm }

def import_gltf(filepath: str):
    _with_bpy()
    prev_objs = set(bpy.data.objects.keys())
    bpy.ops.import_scene.gltf(filepath=filepath)
    new_objs = [bpy.data.objects[name] for name in bpy.data.objects.keys() if name not in prev_objs]
    arm = next((o for o in new_objs if o.type == 'ARMATURE'), None)
    return { 'objects': new_objs, 'armature': arm }

def import_rig(filepath: str):
    ext = filepath.lower()
    if ext.endswith('.fbx'):
        return import_fbx(filepath)
    if ext.endswith('.glb') or ext.endswith('.gltf'):
        return import_gltf(filepath)
    raise RuntimeError(f'Unsupported rig format: {filepath}')

def import_animation_fbx(filepath: str):
    _with_bpy()
    # Importing an animation FBX typically creates an armature with an action
    prev_actions = set(bpy.data.actions.keys())
    bpy.ops.import_scene.fbx(filepath=filepath, automatic_bone_orientation=True)
    new_actions = [bpy.data.actions[name] for name in bpy.data.actions.keys() if name not in prev_actions]
    # Return the last/newest action as a heuristic
    action = new_actions[-1] if new_actions else None
    return action
