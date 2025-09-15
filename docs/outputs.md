# Outputs

Folder: `dist/<CharacterName>/`

- job.json — Blender job (camera, lighting, directions, resolution, clips, retargetProfile, animClips)
- plan.json — Blender plan/report (stub or render summary)
- frames_<clip>/dir_<d>/<frame>.png — raw rendered frames
- atlas_<res>_<clip>.json — rects for by-animation layout
- dir_<d>/atlas_<res>_<clip>.json — rects for by-direction layout
- atlas_<...>.png — composed PNG atlas (if Sharp present)
- frames_index.json — index of all sheets with layout + references
- character.meta.json — metadata with per-clip { frames, fps, anchors, events, hitboxes }

Rect JSON shape

- { clip, resolution, directions? or direction, atlas: { width, height }, rects: [{ id, x, y, w, h }], image? }
- id format: `${clip}_${direction}_${frameIndex}`

Frames index

- { layout, resolution, directions, entries: [{ clip, file, direction?, image? }] }
