from dataclasses import dataclass
from .constants import MU_EARTH, DEG2RAD
from .orbits import circular_orbit_velocity
from .transfers import hohmann_delta_v, plane_change_delta_v, combined_burn_delta_v, bielliptic_delta_v

@dataclass
class TransferCase:
    r1_m: float
    r2_m: float
    inc_change_deg: float = 0.0
    mu: float = MU_EARTH

def plan_simple(case: TransferCase) -> dict:
    """
    Plan basic transfers and return a dict with Δv breakdown.
    """
    dv_hoh = hohmann_delta_v(case.mu, case.r1_m, case.r2_m)
    v_node_low = circular_orbit_velocity(case.mu, case.r1_m)
    inc_rad = case.inc_change_deg * DEG2RAD
    dv_plane_low = plane_change_delta_v(v_node_low, inc_rad)

    # Combined at apogee of Hohmann (approx): lower speed → cheaper plane change
    # For simplicity, treat v_apogee ~ v on higher circular orbit
    v_high = circular_orbit_velocity(case.mu, case.r2_m)
    dv_combined_apogee = combined_burn_delta_v(v_high, v_high, inc_rad)

    return {
        "dv_hohmann": dv_hoh,
        "dv_plane_low": dv_plane_low,
        "dv_combined_at_high": dv_combined_apogee,
    }
