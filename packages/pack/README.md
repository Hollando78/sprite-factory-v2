# @sprite-factory/pack

Deterministic rect packer interface (stub) and composition helpers.

- `packFrames(frames)` sorts stably and places frames in a row with 1px padding.
- CLI uses this to generate rect JSON; when `sharp` is available, it composes PNG atlases from rendered frames.

Future

- Implement bin packing (max atlas size, power-of-two), multi-page atlases, heuristics.
