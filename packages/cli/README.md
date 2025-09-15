# @sprite-factory/cli

Node.js CLI for Sprite Factory v2.

Commands

- `sf init` — create default config and folders
- `sf validate <character.json>` — schema-validate character + animation set
- `sf plan <character.json> [--res N] [--directions N] [--emit-job]` — dry-run + optional job emission
- `sf build <character.json> [...]` — build JSON outputs; optionally render frames (Blender) and compose PNG atlases (Sharp)
- `sf bake-meta <dist/character>` — regenerate metadata from animation set

Run

- `node packages/cli/bin/sf`
- Or add to PATH with a package manager; this repo uses direct node invocation for simplicity.
