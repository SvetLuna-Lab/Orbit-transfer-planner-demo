# Orbit-transfer-planner-demo

Delta-v planner for circular-to-circular transfers: **Hohmann**, **bi-elliptic**, and **plane-change** combinations.  
Idealized, impulsive burns; quick trade-off plots. Python **3.10+**.

---

## Repository structure

```text
orbit-transfer-planner-demo/
├─ src/
│  ├─ __init__.py
│  ├─ constants.py
│  ├─ orbits.py
│  ├─ transfers.py
│  ├─ planner.py
│  └─ plot_tradeoffs.py
├─ tests/
│  ├─ __init__.py
│  ├─ test_orbits.py
│  └─ test_transfers.py
├─ figures/
│  └─ .gitkeep
├─ data/
│  └─ sample_cases.csv   # r1_km,r2_km,inc_deg,mu_km3s2 (Earth by default)
├─ README.md
├─ requirements.txt      # pytest, pytest-cov (tests only)
├─ requirements-dev.txt  # optional: matplotlib for plots
├─ .gitignore
└─ CHANGELOG.md


Requirements

Python 3.10+

Runtime deps: none (standard library)

Test deps (install for unit tests):

pip install -r requirements.txt


Dev/plots (optional, for plot_tradeoffs.py):

pip install -r requirements-dev.txt


Quick start

Run tests:

pip install -r requirements.txt
pytest -q


Compute simple transfer plan (Python REPL or script):

from src.planner import TransferCase, plan_simple
from src.constants import R_EARTH

case = TransferCase(
    r1_m=R_EARTH + 200e3,   # 200 km LEO
    r2_m=R_EARTH + 2000e3,  # ~2000 km circular
    inc_change_deg=10.0     # optional plane change
)
print(plan_simple(case))
# -> {'dv_hohmann': ..., 'dv_plane_low': ..., 'dv_combined_at_high': ...}



Generate trade-off figures (saved to figures/):

pip install -r requirements-dev.txt
python -m src.plot_tradeoffs
# figures/dv_vs_target_alt.png
# figures/dv_planechange_vs_inc.png


Data schema (data/sample_cases.csv)

CSV columns (units):

r1_km,r2_km,inc_deg,mu_km3s2

r1_km — initial circular orbit radius, km (R_earth + altitude)

r2_km — target circular orbit radius, km

inc_deg — inclination change in degrees (0 if none)

mu_km3s2 — gravitational parameter, km³/s² (Earth ≈ 398600.4418)

Example:

r1_km,r2_km,inc_deg,mu_km3s2
6578.1363,8378.1363,10,398600.4418
6578.1363,10378.1363,0,398600.4418


What’s inside

src/constants.py — Earth μ, radius, degree/radian helpers (SI)

src/orbits.py — circular velocity, vis-viva

src/transfers.py — Hohmann Δv, plane-change Δv, bi-elliptic Δv

src/planner.py — minimal planner, combined-burn example

src/plot_tradeoffs.py — two quick plots (Δv vs target altitude; plane-change cost vs inclination)

Tests:

tests/test_orbits.py — circular velocity sanity

tests/test_transfers.py — Δv positivity and a bi-elliptic sanity check


Assumptions & limits

Idealized, impulsive burns (no finite burn effects)

Spherical Earth, no J2, no drag

Circular-to-circular transfers

Bi-elliptic only for Δv comparison (no timing optimization)



Versioning

We follow Semantic Versioning. See CHANGELOG.md
.
Initial release: v0.1.0.


License

Choose an OSI license if you plan to open source (e.g., MIT). Add LICENSE and reference it here.
