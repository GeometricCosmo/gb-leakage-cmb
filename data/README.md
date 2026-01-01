# Data Setup for gb-leakage-cmb

This directory documents how to obtain and organize public likelihood data
required for running MCMC fits and ΔS8 scans.

---

## Planck Likelihoods
- **Source**: Planck 2018 likelihood package (PLC v3.0).
- **Download**: [Planck Legacy Archive](https://pla.esac.esa.int/#cosmology)
- **Contents**: high-ℓ TT, TE, EE; low-ℓ TT; lensing.
- **Setup**:
  - Extract into `data/planck/`.
  - Ensure `.clik` files are accessible to MontePython/CosmoMC.
  - Example path: `data/planck/plc_3.0/hi_l/plik_rd12_HM_v22_TT.clik`.

---

## ACT DR6 Likelihoods
- **Source**: ACT DR6 likelihood package (2023 release).
- **Download**: [ACT DR6 data portal](https://lambda.gsfc.nasa.gov/product/act/)
- **Contents**: TT/TE/EE spectra, covariance matrices.
- **Setup**:
  - Place files in `data/act_dr6/`.
  - Update `.ini` or `.param` configs to point to this directory.

---

## SPT-3G Likelihoods
- **Source**: SPT-3G 2018/2020 likelihood package.
- **Download**: [SPT-3G data release](https://lambda.gsfc.nasa.gov/product/spt/)
- **Contents**: TT/TE/EE spectra, covariance matrices.
- **Setup**:
  - Place files in `data/spt3g/`.
  - Update configs accordingly.

---

## Directory Structure
After setup, your `data/` directory should look like:

```
data/
├── planck/
│   └── plc_3.0/...
├── act_dr6/
│   └── ...
├── spt3g/
│   └── ...
```

---

## Notes
- These likelihoods are **public** but require registration or acceptance of license terms.
- Ensure environment variables (`CLIK_PATH`, etc.) are set if required by MontePython/CosmoMC.
- For reproducibility, document the exact version of each likelihood used in your paper.

---
