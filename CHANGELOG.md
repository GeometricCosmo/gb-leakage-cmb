# Changelog
All notable changes to **gb-leakage-cmb** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]
- Polarization extension (TE/EE fits).
- Fisher forecast utilities for CMB‑S4.
- Expanded examples for ACT DR6 and SPT‑3G.
- Publication‑quality plotting styles.

---

## [0.2.0] – 2026-01-01
### Added
- `ROADMAP.md` outlining short‑term and long‑term goals.
- `INSTALL.md` with step‑by‑step environment and likelihood setup.
- `examples/quickstart.md` walkthrough for reproducing figures and results.
- Directory‑level `README.md` files (`analysis`, `plots`, `validation`, `cluster`, `src`, `data`).
- `docs/comparison.md` comparing gb‑leakage‑cmb to CLASS, CAMB, MontePython, HiCLASS.

### Changed
- Polished `requirements.txt` with grouped dependencies and optional packages.
- Updated `docs/theory_notes.md` with improved formatting and LaTeX equations.
- Enhanced `README.md` with clearer Quickstart and outputs section.

---

## [0.1.0] – 2025-12-31
### Added
- Initial commit with repository structure.
- Core leakage patch (`src/`).
- Validation scripts (`validation/`).
- Plotting utilities (`plots/`).
- MCMC drivers and ΔS8 scan (`analysis/`).
- SLURM cluster script (`cluster/`).
- Example config (`examples/run_planck.ini`).
- End‑to‑end reproducibility test (`tests/test_pipeline.py`).
- `CITATION.cff` for citation metadata.
- `CONTRIBUTING.md` for contribution guidelines.
- MIT `LICENSE`.

---
