# Troubleshooting

Install

- npm install times out: increase timeouts (`--fetch-timeout=120000 --fetch-retries=5`), check proxy, or retry.
- Sharp missing: build will skip PNG atlases; install via `npm i` at repo root.

Blender

- `--blender` path incorrect: set `BLENDER_BIN` env or pass full path.
- No frames rendered: import may fail; check `dist/<name>/plan.json` logs, verify rig and anim paths.
- Non-determinism: ensure Eevee TAA is minimal; avoid physics in MVP.

Viewer

- ERR_CONNECTION_RESET via SSH: restart tunnel (`ssh -N -L 5173:127.0.0.1:5173 user@server`), ensure server binds to 127.0.0.1.
- No images drawn: drop PNG atlases along with JSONs, or run via server so it can fetch from `/dist`.

Paths

- Prefer absolute paths inside Blender job; CLI now resolves rig/anim sources to absolute.
