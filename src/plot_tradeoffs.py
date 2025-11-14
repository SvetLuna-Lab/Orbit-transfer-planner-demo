"""
Plot simple trade-offs for orbit transfers.

Figures produced:
- figures/dv_vs_target_alt.png : Total Δv (Hohmann) vs target altitude
- figures/dv_planechange_vs_inc.png : Δv for plane-change at low vs high orbit

Usage:
    python -m src.plot_tradeoffs
"""

import math
import os
from typing import List

import matplotlib.pyplot as plt  # plotting only (dev dependency)

from .constants import MU_EARTH, R_EARTH, DEG2RAD
from .transfers import hohmann_delta_v, plane_change_delta_v
from .orbits import circular_orbit_velocity


def ensure_outdir(path: str = "figures") -> str:
    os.makedirs(path, exist_ok=True)
    return path


def linspace(start: float, stop: float, num: int) -> List[float]:
    """Tiny replacement for numpy.linspace to avoid extra deps."""
    if num <= 1:
        return [start]
    step = (stop - start) / (num - 1)
    return [start + i * step for i in range(num)]


def plot_dv_vs_target_alt(
    r1_m: float,
    alt2_min_m: float = 200e3,
    alt2_max_m: float = 20000e3,
    n: int = 50,
    mu: float = MU_EARTH,
    outdir: str = "figures",
) -> str:
    """Hohmann Δv from r1 → r2 (r2 = R_EARTH + alt2), sweep target altitude."""
    xs_km = []
    ys_dv = []

    for alt2 in linspace(alt2_min_m, alt2_max_m, n):
        r2 = R_EARTH + alt2
        dv = hohmann_delta_v(mu, r1_m, r2)
        xs_km.append(alt2 / 1000.0)
        ys_dv.append(dv)

    plt.figure()
    plt.plot(xs_km, ys_dv, linewidth=2.0)
    plt.xlabel("Target altitude, km")
    plt.ylabel("Total Δv (Hohmann), m/s")
    plt.title("Δv vs Target Altitude (Hohmann)")
    plt.grid(True, which="both", linestyle="--", alpha=0.4)

    ensure_outdir(outdir)
    out_path = os.path.join(outdir, "dv_vs_target_alt.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()
    return out_path


def plot_plane_change_costs(
    r_low_m: float,
    r_high_m: float,
    inc_min_deg: float = 0.0,
    inc_max_deg: float = 30.0,
    n: int = 31,
    mu: float = MU_EARTH,
    outdir: str = "figures",
) -> str:
    """
    Δv for pure plane change as a function of inclination change at
    low circular orbit vs high circular orbit.
    """
    v_low = circular_orbit_velocity(mu, r_low_m)
    v_high = circular_orbit_velocity(mu, r_high_m)

    inc_vals = linspace(inc_min_deg, inc_max_deg, n)
    dv_low = []
    dv_high = []

    for inc_deg in inc_vals:
        inc_rad = inc_deg * DEG2RAD
        dv_low.append(plane_change_delta_v(v_low, inc_rad))
        dv_high.append(plane_change_delta_v(v_high, inc_rad))

    plt.figure()
    plt.plot(inc_vals, dv_low, label=f"At low orbit ({int((r_low_m-R_EARTH)/1000)} km)")
    plt.plot(inc_vals, dv_high, label=f"At high orbit ({int((r_high_m-R_EARTH)/1000)} km)")
    plt.xlabel("Inclination change, deg")
    plt.ylabel("Δv (plane change), m/s")
    plt.title("Plane-change Δv vs Inclination")
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.legend()

    ensure_outdir(outdir)
    out_path = os.path.join(outdir, "dv_planechange_vs_inc.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()
    return out_path


def main() -> None:
    # Example: from 200 km LEO to a sweep of higher altitudes
    r1 = R_EARTH + 200e3
    _p1 = plot_dv_vs_target_alt(r1_m=r1)

    # Plane-change cost comparison between 200 km and 2000 km circular orbits
    r_low = R_EARTH + 200e3
    r_high = R_EARTH + 2000e3
    _p2 = plot_plane_change_costs(r_low_m=r_low, r_high_m=r_high)

    print("Saved figures to ./figures/:")
    print(" - dv_vs_target_alt.png")
    print(" - dv_planechange_vs_inc.png")


if __name__ == "__main__":
    main()
