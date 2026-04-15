---

# 📘 A Single Scale Suppression of Small Scale Power from 5D Gravitational Leakage  
### Phenomenological Fits to CMB and JWST Data  

`https://img.shields.io/badge/version-v2.0.0-blue.svg`  
`https://img.shields.io/badge/status-active-success.svg`  
`https://img.shields.io/badge/license-MIT-green.svg`

---

## 🔄 Project Evolution
This is **Version 2** of the leakage model project.  
- **Version 1** (`gb-leakage-cmb`) focused narrowly on high‑ℓ CMB damping and the \(S_8\) tension.  
- **Version 2** expands the scope to include **JWST early galaxy counts**, **weak‑lensing fits**, and **comparisons to alternative suppression mechanisms**.  

The idea has grown into something far bigger than originally envisioned: a reproducible framework connecting multiple cosmological tensions with a single phenomenological suppression scale.

---

## 📄 Manuscript
The full paper is available here:  
`[Looks like the result wasn't safe to show. Let's switch things up and try something else!]`

---

## ✨ Key Results
- **CMB damping tail**: Δχ² ≈ −10.2 improvement with ACT DR6 + SPT‑3G.  
- **S₈ shift**: Planck’s 0.832 → 0.762, reducing weak‑lensing tension.  
- **JWST halos**: 30–50% excess at \(z \gtrsim 10\), consistent with early counts.  
- **Trade‑offs**: Joint fits incur penalties, mitigated by priors and nonlinear modeling.  

---

## 📂 Repository Layout
- `papers/` — manuscript PDF and Overleaf export (Version 2)  
- `src/` — CLASS/CAMB patches implementing the suppression transfer function  
- `analysis/` — MCMC drivers, ΔS₈ scans, Fisher utilities  
- `plots/` — plotting scripts for transfer functions, residuals, and comparison figures  
- `validation/` — unit tests and quick checks  
- `data/` — helper scripts for public likelihoods  
- `cluster/` — SLURM job scripts for parameter scans  
- `docs/` — theory notes and comparisons  

---

## 🚀 Quickstart
```bash
# Clone repo
git clone https://github.com/GeometricCosmo/gb-leakage-cmb.git
cd gb-leakage-cmb

# Install dependencies
pip install -r requirements.txt

# Run validation
python validation/test_suppression.py

# Generate figures
python make_graphs.py
```

---

## 📜 Citation
If you use this code or results, please cite:

```bibtex
@misc{gb_leakage_cmb_v2,
  author       = {Andre Swart},
  title        = {A Single Scale Suppression of Small Scale Power from 5D Gravitational Leakage: Phenomenological Fits to CMB and JWST Data (Version 2)},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {GitHub repository}
}
```

---

## 🤝 Contributing
Pull requests are welcome! See `CONTRIBUTING.md` for guidelines.  
MIT License — use it, break it, improve it.

---
