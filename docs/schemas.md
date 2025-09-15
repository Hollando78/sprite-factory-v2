# Schemas

Project (`spritefactory.config.json`)

- seed: integer for determinism
- outputDir, cacheDir
- directions: 4/8/16
- projection: isometric|orthographic
- camera: isoAngle, distance, height, orthoScale
- lighting: key/fill/rim intensities and angles
- resolutions: array of ints
- passes: ["beauty","shadow","mask","outline"]
- palette: optional mask channels

Character (`character.json`)

- name, seed
- rig: src, scale, proportions
- skin: albedo, normal (optional)
- equipment: [{ mount, item, layer, secondaryPhysics? }]
- animations: { set, overrides? }
- export: { mode, paperdollLayers?, masterResolution }

Animation Set (`animationset.json`)

- retargetProfile: e.g., mixamo_humanoid
- clips: map of name → { src, loop, frames, fps?, markers? }
