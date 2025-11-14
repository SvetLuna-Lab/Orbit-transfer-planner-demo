import math

def circular_orbit_velocity(mu: float, r: float) -> float:
    """Return circular orbital velocity at radius r (m/s)."""
    return math.sqrt(mu / r)

def vis_viva(mu: float, r: float, a: float) -> float:
    """Vis-viva equation: v^2 = mu*(2/r - 1/a)."""
    return math.sqrt(mu * (2.0 / r - 1.0 / a))
