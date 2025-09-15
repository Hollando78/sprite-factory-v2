# @sprite-factory/web-server

Minimal Node server to host the QA viewer and `/dist/` outputs.

Run

- `node packages/web-server/bin/sf-web`
- Binds to `127.0.0.1:5173` by default; override with `HOST`/`PORT`.

API

- `GET /api/characters` — list characters (directories) under `dist/`
- `GET /api/characters/:name/meta` — `character.meta.json`
- `GET /api/characters/:name/frames_index` — `frames_index.json`

Static

- `/` — QA viewer
- `/dist/...` — static files from `dist/`
