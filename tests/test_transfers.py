from src.constants import MU_EARTH, R_EARTH
from src.transfers import hohmann_delta_v, bielliptic_delta_v

def test_hohmann_positive():
    r1 = R_EARTH + 200e3
    r2 = R_EARTH + 2000e3
    dv = hohmann_delta_v(MU_EARTH, r1, r2)
    assert dv > 0.0

def test_bielliptic_not_worse_for_small_ratio():
    r1 = R_EARTH + 200e3
    r2 = R_EARTH + 300e3
    dv_bi = bielliptic_delta_v(MU_EARTH, r1, r2, r_b=R_EARTH + 10000e3)
    dv_ho = hohmann_delta_v(MU_EARTH, r1, r2)
    assert dv_bi >= dv_ho  # for close orbits bi-elliptic usually not beneficial
