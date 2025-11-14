import math

def hohmann_delta_v(mu: float, r1: float, r2: float) -> float:
    """
    Total Δv for Hohmann transfer between circular orbits r1 -> r2.
    Returns Δv_total [m/s].
    """
    a_t = 0.5 * (r1 + r2)
    v1 = math.sqrt(mu / r1)
    v2 = math.sqrt(mu / r2)
    v_peri = math.sqrt(mu * (2.0 / r1 - 1.0 / a_t))
    v_apo  = math.sqrt(mu * (2.0 / r2 - 1.0 / a_t))
    dv1 = abs(v_peri - v1)
    dv2 = abs(v2 - v_apo)
    return dv1 + dv2

def plane_change_delta_v(v: float, inc_change_rad: float) -> float:
    """
    Pure plane-change burn at speed v with inclination change Δi (rad).
    Δv = 2 v sin(Δi/2)
    """
    return 2.0 * v * math.sin(0.5 * inc_change_rad)

def combined_burn_delta_v(v1: float, v2: float, inc_change_rad: float) -> float:
    """
    Combine transfer and plane-change at a single node:
    Δv = sqrt(v1^2 + v2^2 - 2 v1 v2 cos(Δi))
    """
    return math.sqrt(v1*v1 + v2*v2 - 2.0*v1*v2*math.cos(inc_change_rad))

def bielliptic_delta_v(mu: float, r1: float, r2: float, r_b: float) -> float:
    """
    Bi-elliptic transfer total Δv with intermediate apogee r_b (r_b > max(r1,r2)).
    Returns Δv_total [m/s].
    """
    # Leg 1: r1 -> rb
    a1 = 0.5 * (r1 + r_b)
    v_c1 = math.sqrt(mu / r1)
    v_p1 = math.sqrt(mu * (2.0 / r1 - 1.0 / a1))
    dv1 = abs(v_p1 - v_c1)

    # At rb: change velocity to match ellipse to r2
    a2 = 0.5 * (r_b + r2)
    v_a1 = math.sqrt(mu * (2.0 / r_b - 1.0 / a1))
    v_a2 = math.sqrt(mu * (2.0 / r_b - 1.0 / a2))
    dv2 = abs(v_a2 - v_a1)

    # Leg 3: rb -> r2
    v_c2 = math.sqrt(mu / r2)
    v_p2 = math.sqrt(mu * (2.0 / r2 - 1.0 / a2))
    dv3 = abs(v_c2 - v_p2)

    return dv1 + dv2 + dv3
