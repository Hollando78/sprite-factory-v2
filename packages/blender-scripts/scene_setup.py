import math

ISO_TILT_DEG = 35.26438968  # arcsin(tan(35.264..)) ~ true iso

def iso_camera_settings(projection: str = 'isometric', camera_cfg: dict | None = None):
    camera_cfg = camera_cfg or {}
    if projection == 'isometric':
        tilt = ISO_TILT_DEG
        yaw = 45.0
        ortho_scale = float(camera_cfg.get('orthoScale', 2.0))
        return {
            'projection': 'ORTHO',
            'tilt_deg': tilt,
            'yaw_deg': yaw,
            'ortho_scale': ortho_scale,
            'distance': float(camera_cfg.get('distance', 8.5)),
            'height': float(camera_cfg.get('height', 1.7)),
        }
    else:
        tilt = float(camera_cfg.get('isoAngle', 30.0))
        yaw = 45.0
        ortho_scale = float(camera_cfg.get('orthoScale', 2.0))
        return {
            'projection': 'ORTHO',
            'tilt_deg': tilt,
            'yaw_deg': yaw,
            'ortho_scale': ortho_scale,
            'distance': float(camera_cfg.get('distance', 8.5)),
            'height': float(camera_cfg.get('height', 1.7)),
        }

def compute_direction_angles(directions: int):
    step = 360.0 / max(1, int(directions) or 8)
    return [(i * step) % 360.0 for i in range(int(directions))]

def setup_scene():
    # Placeholder for camera/lights/collections setup
    return True
