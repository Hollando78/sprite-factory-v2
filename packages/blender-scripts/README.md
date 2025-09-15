@sprite-factory/blender-scripts — headless Blender entry and helpers.

Entrypoint

- `main.py` — parse `--job` JSON; run as stub (python) or with Blender (bpy) to render frames.

Helpers

- `scene_setup.py` — iso camera defaults and direction angles
- `import_assets.py` — import rig (FBX/GLTF) and animation clips (FBX)
- `render_turntable.py` — compute direction angles (placeholder)

Run

- Blender: `blender -b -P packages/blender-scripts/main.py -- --job dist/<name>/job.json`
- Stub: `python3 packages/blender-scripts/main.py -- --job dist/<name>/job.json`
