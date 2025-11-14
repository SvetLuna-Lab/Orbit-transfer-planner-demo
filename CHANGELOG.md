# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- (placeholder) Add Lambert solver option.
- (placeholder) Add porkchop-style visualization for departure/arrival dates.

### Changed
- (placeholder) Refactor transfers API for extensibility.

### Fixed
- (placeholder) Numerical stability for high eccentricity cases.

---

## [0.1.0] - 2025-11-14
### Added
- Initial repository skeleton: `src/`, `tests/`, `figures/`, `data/`.
- Core math:
  - `src/constants.py` (Earth μ, radius, degree/radian helpers).
  - `src/orbits.py` (circular velocity, vis-viva).
  - `src/transfers.py` (Hohmann, plane-change, bi-elliptic Δv).
  - `src/planner.py` (simple planner + combined burns example).
  - `src/plot_tradeoffs.py` (Δv vs altitude; plane-change cost vs inclination).
- Tests:
  - `tests/test_orbits.py`, `tests/test_transfers.py` (smoke + sanity checks).
- Data:
  - `data/sample_cases.csv` schema for Δv planning.
- Docs:
  - Minimal `README.md` with quick start and example.
- CI/Dev:
  - `requirements.txt` (pytest only), `.gitignore`, `figures/.gitkeep`.

### Changed
- N/A (initial release)

### Fixed
- N/A (initial release)

[Unreleased]: https://github.com/<ORG_OR_USER>/orbit-transfer-planner-demo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/<ORG_OR_USER>/orbit-transfer-planner-demo/releases/tag/v0.1.0
