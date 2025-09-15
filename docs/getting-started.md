# Getting Started

Prereqs

- Node.js 18+ (22 OK)
- Optional: Blender 4.x (headless rendering)

Install

- npm install (at repo root)

First run

- Plan: `node packages/cli/bin/sf plan samples/characters/warrior.json --res 64 --directions 8`
- Build (JSON-only): `node packages/cli/bin/sf build samples/characters/warrior.json --res 64 --directions 8 --no-blender`
- Build with Blender: set `BLENDER_BIN` or pass `--blender` with path.

View results

- Start server: `node packages/web-server/bin/sf-web`
- Open: `http://127.0.0.1:5173/?character=Warrior_M01`

SSH tunnel

- Local forward: `ssh -N -L 5173:127.0.0.1:5173 user@server`
- Open `http://127.0.0.1:5173/?character=Warrior_M01`

Next steps

- See `docs/cli.md` for commands and flags
- See `docs/blender.md` for Blender rendering details
