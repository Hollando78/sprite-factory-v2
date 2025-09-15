# Sprite Factory v2 — Monorepo

Deterministic pipeline to turn rigged 3D characters + animations into 2D sprite atlases and metadata.

- CLI: init/validate/plan/build/bake-meta
- Blender headless scripts: scene setup, import, turntable rendering
- Schemas: project, character, animation set
- Packer: deterministic rect packing (stub) + optional PNG atlas composition
- QA viewer: inspect frames, events, anchors, hitboxes
- Web server: hosts viewer and `dist/` outputs for easy browsing

Repository layout

- packages/cli — `sf` CLI (Node.js)
- packages/schemas — JSON Schemas (project/character/animationset)
- packages/blender-scripts — Blender entry + helpers (Python)
- packages/pack — deterministic packer (stub) and API
- packages/qa-viewer — static viewer (no build step)
- packages/web-server — static server for viewer + dist
- samples/ — example configs and sets
- content/ — rigs, anims, gear placeholders

Requirements

- Node.js 18+ (works on Node 22 as well)
- Optional: Blender 4.x for rendering (headless)
- Optional: `sharp` for PNG atlas composition (installed automatically via npm)

Quick start

- Install deps: `npm install` (at repo root)
- CLI help: `node packages/cli/bin/sf`
- Plan: `node packages/cli/bin/sf plan samples/characters/warrior.json --res 64 --directions 8`
- Build (JSON-only): `node packages/cli/bin/sf build samples/characters/warrior.json --res 64 --directions 8 --no-blender`
- Build with Blender:
  - macOS/Linux: `BLENDER_BIN="/path/to/blender" node packages/cli/bin/sf build samples/characters/warrior.json --res 64 --directions 8`
  - Windows: `node packages\cli\bin\sf build samples\characters\warrior.json --res 64 --directions 8 --blender "C:\\Program Files\\Blender Foundation\\Blender\\blender.exe"`
- Serve viewer: `node packages/web-server/bin/sf-web` then open `http://127.0.0.1:5173/?character=Warrior_M01`

Documentation

- docs/getting-started.md — setup, install, workflow
- docs/cli.md — commands and flags
- docs/schemas.md — config model
- docs/outputs.md — generated files and formats
- docs/blender.md — headless rendering details
- docs/qa-viewer.md — usage and features
- docs/troubleshooting.md — common issues

Status

MVP scaffolding is implemented. Rendering integrates with Blender for frame export; PNG atlas composition runs when Sharp is available. Viewer supports PNG atlases and metadata overlays. See Backlog in the design doc for remaining features.
