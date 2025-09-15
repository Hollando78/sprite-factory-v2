# @sprite-factory/qa-viewer

Static HTML/JS viewer for atlases and metadata.

Open

- `packages/qa-viewer/index.html`
- or via server: `node packages/web-server/bin/sf-web` → `http://127.0.0.1:5173/?character=<Name>`

Features

- Draws atlas PNGs and overlays anchors, hitboxes, events; timeline markers
- Supports `by-animation` and `by-direction` layouts
- Drag/drop JSON+PNG or auto-fetch from `/dist/<Name>/...`
