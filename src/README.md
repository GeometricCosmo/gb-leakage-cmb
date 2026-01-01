# Source Code: Leakage Patches

This directory contains the core code modifications that implement the Gauss–Bonnet leakage model in CAMB/CLASS.

---

## 📂 Files

### `camb_leakage_patch.py`
- **Purpose**: Python wrapper to apply leakage suppression to CAMB spectra.
- **Implementation**:
  - Modifies the primordial power spectrum:
    \[
    P_{\rm mod}(k) = P_{\rm prim}(k) \cdot T(k)^2
    \]
  - Transfer function:
    \[
    T(k) = \exp\left[-\left(\frac{k}{k_c}\right)^p\right]
    \]
- **Usage**:
  ```bash
  python src/camb_leakage_patch.py --kc 0.75 --p 2.5
  ```
- **Outputs**:
  - Modified spectra saved in `results/`.
  - Can be imported by analysis scripts.

---

## 🧩 Workflow

1. **Patch CAMB/CLASS**:  
   The leakage function is injected into the primordial spectrum calculation.
2. **Validation**:  
   Compare analytic suppression with CAMB outputs (`validation/test_suppression.py`).
3. **Analysis**:  
   Use patched spectra in ΔS8 scans (`analysis/compute_delta_S8.py`) and MCMC fits (`analysis/run_mcmc.py`).

---

## 📌 Notes
- Requires CAMB installed with Python bindings.
- Parameters:
  - `kc`: cutoff scale in Mpc⁻¹
  - `p`: exponent controlling suppression strength
- Extendable: Developers can add new phenomenological models by creating additional patch files in `src/`.

---
