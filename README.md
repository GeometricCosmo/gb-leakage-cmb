# gb-leakage-cmb

A simple, physical fix for the high-ℓ CMB damping and the σ₈/S₈ tension without new particles.

![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)

This repo adds one smooth, Gauss‑Bonnet inspired transfer function `T(k)` to the primordial power spectrum. It suppresses small‑scale power just enough to:
- Remove the ~3σ preference for extra smoothing in Planck/ACT/SPT data
- Lower σ₈ by ~0.07 → brings weak lensing and clusters into agreement
- Keep all the big successes of ΛCDM untouched

## Features
- Drop‑in patches for CLASS and CAMB  
- Simulate a slice from the early universe; this paper shows the smudge is not on the lens but is a physical feature  
- Ready to run MontePython and Cobaya likelihoods  
- Full chains with Planck 2018 + ACT DR6 + SPT‑3G (or input your own values)  
- MIT license — grab it, break it, improve it

Phenomenological Gauss–Bonnet braneworld leakage model for high‑ℓ CMB suppression.  
Includes CAMB/CLASS patches, MCMC scripts, and reproducible pipelines for Planck, ACT DR6, and SPT‑3G data.

---

## 📄 Manuscript

You can view or download the full paper here:  
[Gauss–Bonnet Motivated Phenomenological Model for High‑ℓ CMB Power Suppression (PDF)](GB_CMB_Suppression.pdf)

---

## GB Leakage Model for High‑ℓ CMB Suppression

This repository provides a reproducible pipeline to test a phenomenological,
Gauss‑Bonnet inspired leakage model for high‑ℓ CMB power suppression.

---

## 📂 Contents
- `src/` : CAMB/CLASS patches implementing  
  

\[
  P_{\rm mod}(k) = P_{\rm prim}(k) \cdot T(k)^2
  \]


- `analysis/` : MCMC driver wrappers, ΔS8 scans, Fisher forecast utilities
- `plots/` : plotting utilities for transfer, residuals, and corner plots
- `validation/` : unit tests validating suppression behavior
- `cluster/` : SLURM array script for large parameter scans
- `data/` : helper script to document/download public likelihoods
- `docs/` : theory notes and assumptions

---

## 🚀 Quickstart

### 1. Clone
```bash
git clone https://github.com/GeometricCosmo/gb-leakage-cmb.git
cd gb-leakage-cmb
2. Install dependencies
bash
pip install -r requirements.txt
⚠️ Note: You must have CAMB installed with Python bindings.
For MCMC fits, install MontePython or CosmoMC separately.

3. Run validation
Check that the leakage patch reproduces the analytic suppression:

bash
python validation/test_suppression.py
4. Generate figures
Analytic envelope (Appendix):

bash
python notebooks/validation_quick.py
Transfer function T(k):

bash
python plots/plot_transfer.py
Residual ratio C_\ell^{\rm mod}/C_\ell^{\Lambda{\rm CDM}}:

bash
python plots/plot_residuals.py
ΔS8 scan:

bash
python analysis/compute_delta_S8.py --p 2.0 --nproc 8 --outdir results
Corner plot (from chains):

bash
python plots/plot_corner.py
5. Run MCMC fits
Toy example (local run):

bash
python analysis/run_mcmc.py --engine cosmomc --kc 0.75 --p 2.5 --nprocs 4
Cluster scan (SLURM array job):

bash
sbatch cluster/slurm_run_fits.sh
6. Outputs
Figures saved in figures/

ΔS8 results in results/delta_s8_summary.npz

Chains in chains/

📖 Documentation
Theory background: docs/theory_notes.md

Comparison to related repos: docs/comparison.md (coming soon)

📜 Citation
If you use this code in your work, please cite:

bibtex
@misc{gb_leakage_cmb,
  author       = {Andre Swart},
  title        = {gb-leakage-cmb: Gauss–Bonnet Leakage Model for High-ℓ CMB Suppression},
  year         = {2025/2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/GeometricCosmo/gb-leakage-cmb}}
}
🤝 Contributing
Pull requests are welcome! See CONTRIBUTING.md for guidelines.

📌 License
This project is licensed under the MIT License — see LICENSE for details.

So use it, break it, make it better!

Code

---
---

So use it, break it, make it better!



### Quick commands to fix the PDF filename and update README

1. Rename the PDF in your local clone (fix the double `.pdf`):
```bash
git mv GaussBonnet_CMB_Suppression.pdf.pdf GB_CMB_Suppression.pdf
git commit -m "Rename manuscript to GB_CMB_Suppression.pdf"
