import math
from src.constants import MU_EARTH, R_EARTH
from src.orbits import circular_orbit_velocity

def test_circular_velocity_monotonic():
    v_low = circular_orbit_velocity(MU_EARTH, R_EARTH + 200e3)
    v_high = circular_orbit_velocity(MU_EARTH, R_EARTH + 2000e3)
    assert v_low > v_high and v_low > 7000.0 and v_high > 6000.0
