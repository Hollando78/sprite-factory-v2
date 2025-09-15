# CLI Reference (sf)

Usage

- `sf init` — scaffold project folders and default `spritefactory.config.json`
- `sf validate <character.json>` — validate character and animation set against schemas; check referenced files
- `sf plan <character.json> [--res N] [--directions N] [--emit-job]` — print plan; optionally write Blender job
- `sf build <character.json> [--res N] [--directions N] [--projection P] [--layout L] [--only clip] [--no-blender] [--blender PATH]` — build JSON, optionally render frames and compose PNG atlases
- `sf bake-meta <dist/character>` — regenerate metadata from existing outputs

Flags

- `--res` master resolution per frame (px)
- `--directions` number of directions (4,8,16)
- `--projection` `orthographic` or `isometric`
- `--layout` `by-animation` (default) or `by-direction`
- `--only` filter to a single clip
- `--emit-job` write `job.json` in output folder
- `--no-blender` skip Blender (JSON-only)
- `--blender` path to Blender binary (or set `BLENDER_BIN`)

Outputs

- `dist/<name>/job.json` — Blender job
- `dist/<name>/plan.json` — Blender plan (stub or after render)
- `dist/<name>/frames_<clip>/dir_<d>/<frame>.png` — rendered PNG frames (when Blender used)
- `dist/<name>/atlas_*.json` — rects for packed sheets
- `dist/<name>/atlas_*.png` — composed PNG atlases (if Sharp available)
- `dist/<name>/frames_index.json` — index of sheets
- `dist/<name>/character.meta.json` — metadata (anchors/events/hitboxes)
