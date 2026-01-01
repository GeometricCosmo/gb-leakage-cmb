# Quickstart Examples for gb-leakage-cmb

This guide provides step‑by‑step instructions to reproduce the figures and results from the paper using the scripts in this repository.  
It complements the main `README.md` by showing concrete commands and expected outputs.

---

## 1. Validation
Check that the leakage patch reproduces the analytic suppression:
```bash
python validation/test_suppression.py
```
Expected output: confirmation message in terminal.

---

## 2. Analytic Envelope (Appendix)
Generate the analytic suppression envelope \(T(k)^2\) vs multipole:
```bash
python notebooks/validation_quick.py
```
Output:  
- `figures/validation_quick.png`

---

## 3. Transfer Function
Plot the transfer function \(T(k)\):
```bash
python plots/plot_transfer.py
```
Output:  
- `figures/transfer_function.png`

---

## 4. Residual Ratio
Compare modified vs baseline spectra:
```bash
python plots/plot_residuals.py
```
Output:  
- `figures/tt_residual_ratio.png`

---

## 5. ΔS8 Scan
Run a parallel scan over \(k_c\):
```bash
python analysis/compute_delta_S8.py --p 2.0 --nproc 8 --outdir results
```
Outputs:  
- `results/delta_s8_summary.npz` (numerical data)  
- `results/delta_S8_vs_kc.png` (plot)

---

## 6. Corner Plot
Generate posterior corner plots for \((k_c, p)\):
```bash
python plots/plot_corner.py
```
Output:  
- `figures/corner_kc_p.png`

---

## 7. MCMC Fits
Toy example (local run):
```bash
python analysis/run_mcmc.py --engine cosmomc --kc 0.75 --p 2.5 --nprocs 4
```

Cluster scan (SLURM array job):
```bash
sbatch cluster/slurm_run_fits.sh
```

Outputs:  
- Chains in `chains/`  
- Figures in `figures/`

---

## Notes
- Ensure CAMB is installed with Python bindings.  
- For MCMC fits, install MontePython or CosmoMC separately.  
- Figures are saved in `figures/`, results in `results/`, chains in `chains/`.  

📖 For theoretical background, see [`docs/theory_notes.md`](../docs/theory_notes.md).
```
