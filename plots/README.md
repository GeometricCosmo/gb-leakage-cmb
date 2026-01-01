# Plotting Utilities for gb-leakage-cmb

This directory contains scripts to generate figures for the paper and validation
of the Gauss–Bonnet leakage model.

---

## 📂 Scripts

### `plot_transfer.py`
- **Purpose**: Plot the leakage transfer function \(T(k)\) for chosen parameters \((k_c, p)\).
- **Usage**:
  ```bash
  python plots/plot_transfer.py
  ```
- **Output**: `figures/transfer_function.png`

---

### `plot_residuals.py`
- **Purpose**: Plot the residual ratio \(C_\ell^{\rm mod}/C_\ell^{\Lambda{\rm CDM}}\) showing suppression at high ℓ.
- **Usage**:
  ```bash
  python plots/plot_residuals.py
  ```
- **Output**: `figures/tt_residual_ratio.png`
- **Note**: Requires CAMB installed with Python bindings.

---

### `plot_corner.py`
- **Purpose**: Generate posterior corner plots for leakage parameters \((k_c, p)\).
- **Usage**:
  ```bash
  python plots/plot_corner.py
  ```
- **Output**: `figures/corner_kc_p.png`
- **Note**: Replace synthetic samples with real MCMC chain outputs for publication.

---

## 🧩 Workflow

1. Run validation (`validation/test_suppression.py`).
2. Generate transfer function (`plot_transfer.py`).
3. Generate residual ratio (`plot_residuals.py`).
4. Run MCMC fits (`analysis/run_mcmc.py`).
5. Generate corner plot (`plot_corner.py`).

---

## 📌 Notes
- All figures are saved in the `figures/` directory.
- Ensure CAMB and likelihood data are installed before running residual plots.
- Corner plots require chain outputs in `chains/`.

---
