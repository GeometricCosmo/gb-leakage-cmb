# gb-leakage-cmb
Phenomenological Gauss–Bonnet braneworld leakage model for high‑ℓ CMB suppression.  
Includes CAMB/CLASS patches, MCMC scripts, and reproducible pipelines for Planck, ACT DR6, and SPT‑3G data.

---

## GB Leakage Model for High-ℓ CMB Suppression

This repository provides a reproducible pipeline to test a phenomenological,
Gauss–Bonnet–inspired leakage model for high-ℓ CMB power suppression.

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
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
> ⚠️ Note: You must have [CAMB](https://github.com/cmbant/CAMB) installed with Python bindings.  
> For MCMC fits, install [MontePython](https://github.com/brinckmann/montepython_public) or CosmoMC separately.

### 3. Run validation
Check that the leakage patch reproduces the analytic suppression:
```bash
python validation/test_suppression.py
```

### 4. Generate figures
- Analytic envelope (Appendix):
  ```bash
  python notebooks/validation_quick.py
  ```
- Transfer function \(T(k)\):
  ```bash
  python plots/plot_transfer.py
  ```
- Residual ratio \(C_\ell^{\rm mod}/C_\ell^{\Lambda{\rm CDM}}\):
  ```bash
  python plots/plot_residuals.py
  ```
- ΔS8 scan:
  ```bash
  python analysis/compute_delta_S8.py --p 2.0 --nproc 8 --outdir results
  ```
- Corner plot (from chains):
  ```bash
  python plots/plot_corner.py
  ```

### 5. Run MCMC fits
Toy example (local run):
```bash
python analysis/run_mcmc.py --engine cosmomc --kc 0.75 --p 2.5 --nprocs 4
```

Cluster scan (SLURM array job):
```bash
sbatch cluster/slurm_run_fits.sh
```

### 6. Outputs
- Figures saved in `figures/`
- ΔS8 results in `results/delta_s8_summary.npz`
- Chains in `chains/`

---

## 📖 Documentation
- Theory background: [`docs/theory_notes.md`](docs/theory_notes.md)
- Comparison to related repos: [`docs/comparison.md`](docs/comparison.md) *(coming soon)*

---

## 📜 Citation
If you use this code in your work, please cite:

```
@misc{gb_leakage_cmb,
  author       = {Andre and collaborators},
  title        = {gb-leakage-cmb: Gauss–Bonnet Leakage Model for High-ℓ CMB Suppression},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/GeometricCosmo/gb-leakage-cmb}}
}
```

---

## 🤝 Contributing
Pull requests are welcome! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## 📌 License
This project is licensed under the MIT License – see [`LICENSE`](LICENSE) for details.
```

---
