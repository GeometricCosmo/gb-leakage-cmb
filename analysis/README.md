# Analysis Scripts for gb-leakage-cmb

This directory contains analysis utilities for scanning leakage parameters,
computing ΔS8, and running MCMC fits with Planck/ACT/SPT likelihoods.

---

## 📂 Scripts

### `compute_delta_S8.py`
- **Purpose**: Scans over cutoff scale `kc` for fixed exponent `p` to compute ΔS8.
- **Usage**:
  ```bash
  python compute_delta_S8.py --p 2.0 --nproc 8 --outdir results
  ```
- **Outputs**:
  - `results/delta_s8_summary.npz` (numerical data)
  - `results/delta_S8_vs_kc.png` (plot)

---

### `run_mcmc.py`
- **Purpose**: Wrapper to launch MCMC fits with leakage parameters.
- **Engines**: Supports `cosmomc` or `montepython`.
- **Usage**:
  ```bash
  python run_mcmc.py --engine cosmomc --kc 0.75 --p 2.5 --nprocs 4
  ```
- **Outputs**:
  - Chains in `chains/`
  - Figures in `figures/`

---

### `fisher_forecast.py` *(planned)*
- **Purpose**: Fisher matrix forecasts for leakage parameters with CMB‑S4‑like data.
- **Status**: Placeholder for future development.

---

## 🧩 Workflow

1. **Validation**: Run `validation/test_suppression.py` to confirm leakage patch.
2. **ΔS8 Scan**: Use `compute_delta_S8.py` for suppression impact on S8.
3. **MCMC Fits**: Run `run_mcmc.py` for posterior inference on `(kc, p)`.
4. **Forecasts**: (optional) Extend with `fisher_forecast.py`.

---

## 📌 Notes
- Requires CAMB installed with Python bindings.
- Likelihood data must be placed in `data/` (see `data/README.md`).
- Outputs are saved in `results/` and `chains/`.

---
