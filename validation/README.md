# Validation Utilities for gb-leakage-cmb

This directory contains unit tests and quick validation scripts to confirm that
the Gauss–Bonnet leakage patch behaves as expected.

---

## 📂 Scripts

### `test_suppression.py`
- **Purpose**: Unit test comparing analytic suppression envelope with CAMB‑patched spectra.
- **Usage**:
  ```bash
  python validation/test_suppression.py
  ```
- **Output**: Terminal confirmation message (e.g., "Suppression test passed").
- **Note**: Requires CAMB installed with Python bindings.

---

### `validation_quick.py`
- **Purpose**: Quick analytic visualization of suppression envelope \(T(k)^2\) vs multipole.
- **Usage**:
  ```bash
  python notebooks/validation_quick.py
  ```
- **Output**: `figures/validation_quick.png`
- **Note**: Uses synthetic analytic formula, no CAMB required.

---

## 🧩 Workflow

1. Run `test_suppression.py` to confirm CAMB patch matches analytic suppression.
2. Run `validation_quick.py` to generate a quick figure for the appendix.
3. Proceed to plotting scripts in `plots/` for transfer/residual/corner figures.

---

## 📌 Notes
- Validation scripts are lightweight and can be run on a laptop.
- They provide reproducibility checks for referees and collaborators.
- All figures are saved in `figures/`.

---
