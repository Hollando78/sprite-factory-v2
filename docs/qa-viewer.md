# QA Viewer

Open

- Static file: `packages/qa-viewer/index.html`
- Via server: `node packages/web-server/bin/sf-web` → `http://127.0.0.1:5173/?character=<Name>`

Features

- Load `frames_index.json`, `atlas_*.json`, `character.meta.json`
- Auto-fetch from `/dist/<Name>/...` when `?character=<Name>` is present
- Draw atlas PNGs when available; otherwise shows frame bounds
- Overlays: anchors, hitboxes, events; timeline markers
- Controls: clip, direction, frame, FPS, play/pause

Planned

- Editing anchors/hitboxes/events and export updated metadata
- Paper-doll layering preview
