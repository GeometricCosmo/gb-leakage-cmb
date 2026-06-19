# Analysis Scripts: gb-leakage-cmb

**Comprehensive utilities for parameter scanning, ΔS8 computation, and MCMC inference on radion-EM coupling and leakage parameters.**

---

## 📋 Quick Overview

This directory contains analysis tools for:
- **ΔS8 Sensitivity Scans** — Measure how different leakage parameters affect S₈ predictions
- **MCMC Posterior Inference** — Constrain leakage parameters from CMB/weak-lensing/Lyman-α data
- **Fisher Forecasts** — Predict constraining power for future surveys (CMB-S4, etc.)
- **Parameter Validation** — Check consistency across different observables

**Typical workflow:**
```
Validation
    ↓
ΔS8 parameter scan
    ↓
MCMC inference
    ↓
Results analysis & plotting
    ↓
Publication figures
```

---

## 🧱 Connection to Seven-Brick Framework

These scripts validate the seven bricks through observational comparison:

| Brick | Script | What's Tested |
|-------|--------|--------------|
| **Brick 1** | All scripts | EM coupling (fixed in code) |
| **Brick 2** | `compute_delta_S8.py` | Radion dynamics → leakage fraction |
| **Brick 3** | `compute_delta_S8.py` | Gravity modification ($G_{\text{eff}}$) |
| **Brick 4** | `compute_delta_S8.py` | Scale selection ($k_c \approx 0.75$) |
| **Brick 5** | `run_mcmc.py` | Cosmological predictions vs data |
| **Brick 6** | Validation phase | Stability checks |
| **Brick 7** | (Future) | Lab signature forecasts |

---

## 📊 Script Directory

### **`compute_delta_S8.py`** — Parameter Sensitivity Scan

**Purpose:** Measure how σ₈ (matter clustering) varies with leakage parameters.

**What it does:**
1. Loads baseline CAMB model (ΛCDM)
2. Computes σ₈ at different transfer function cutoff scales ($k_c$)
3. Computes σ₈ for different power-law exponents ($p$)
4. Scans over parameter grid
5. Outputs sensitivity curve and data table

**Usage:**

```bash
# Basic: scan kc for fixed p
python analysis/compute_delta_S8.py \
    --p 2.0 \
    --kc_min 0.1 \
    --kc_max 2.0 \
    --nkc 50 \
    --nproc 8 \
    --outdir results/delta_s8/

# Scan both kc and p
python analysis/compute_delta_S8.py \
    --scan_mode 2d \
    --p_min 1.5 \
    --p_max 3.0 \
    --np 10 \
    --kc_min 0.1 \
    --kc_max 2.0 \
    --nkc 30 \
    --nproc 8 \
    --outdir results/delta_s8_2d/

# Quick test run (reduced resolution)
python analysis/compute_delta_S8.py \
    --p 2.0 \
    --nkc 5 \
    --quick \
    --outdir results/test/
```

**Command-line arguments:**

```
Scanning parameters:
  --p FLOAT               Fixed exponent (default: 2.0)
  --kc_min FLOAT         Min cutoff scale h/Mpc (default: 0.1)
  --kc_max FLOAT         Max cutoff scale h/Mpc (default: 2.0)
  --nkc INT              Number of kc points (default: 50)
  --scan_mode STR        '1d' or '2d' scan (default: '1d')
  --p_min FLOAT          Min p for 2D scan (default: 1.5)
  --p_max FLOAT          Max p for 2D scan (default: 3.0)
  --np INT               Number of p points (default: 10)

Performance:
  --nproc INT            Number of parallel processes (default: 4)
  --camb_acc INT         CAMB accuracy setting (default: 1)

Output:
  --outdir STR           Output directory (default: results/)
  --verbose BOOL         Verbose output (default: True)
  --quick BOOL           Quick test mode (default: False)
```

**Outputs:**

```
results/delta_s8/
├── config.json                    # Parameters used in scan
├── delta_s8_summary.npz           # Numerical results (NumPy archive)
│   ├── kc                         # Cutoff scales tested
│   ├── sigma8_baseline            # ΛCDM σ₈ values
│   ├── sigma8_model               # Model σ₈ values
│   └── delta_s8                   # ΔS₈ = |σ₈_baseline - σ₈_model|
├── delta_S8_vs_kc.png             # Publication-quality plot
├── delta_S8_vs_kc_comparison.txt  # ASCII table for reading
└── scan_log.txt                   # Execution log
```

**Output interpretation:**

```python
# Load results
import numpy as np

data = np.load('results/delta_s8/delta_s8_summary.npz')
kc = data['kc']
delta_s8 = data['delta_s8']

# Find best-fit region
best_kc = kc[np.argmin(np.abs(delta_s8 - 0.02))]  # ΔS₈ ≈ 2% suppression
print(f"Best-fit kc: {best_kc:.3f} h/Mpc")

# Compare to observational constraints
# Planck 2018 + DES Y3: ΔS₈ ≈ 0.02–0.03
if np.min(delta_s8) < 0.03:
    print("Model can explain observed S₈ tension ✓")
else:
    print("Model cannot explain S₈ tension ✗")
```

**Performance tips:**

```bash
# For quick testing
--nkc 10 --nproc 8        # ~2 minutes

# For publication-quality results
--nkc 100 --nproc 16      # ~20 minutes

# For 2D scans (slower)
--scan_mode 2d --nkc 50 --np 30 --nproc 32  # ~2 hours
```

---

### **`run_mcmc.py`** — MCMC Parameter Inference

**Purpose:** Perform Bayesian inference on leakage parameters using CMB, weak-lensing, and Lyman-α data.

**What it does:**
1. Sets up likelihood (Planck/ACT/SPT/DES/DESI)
2. Defines prior on leakage parameters ($k_c$, $p$, etc.)
3. Launches MCMC sampler (MontePython or CosmoMC)
4. Monitors convergence
5. Produces posterior samples and convergence plots

**Usage:**

```bash
# Simple: Planck only (quick test)
python analysis/run_mcmc.py \
    --config examples/test_planck_only.ini \
    --n_steps 1000 \
    --n_chains 4 \
    --outdir results/mcmc_planck/

# Full analysis: Planck + ACT + SPT + DES + DESI
python analysis/run_mcmc.py \
    --config examples/run_full_suite.ini \
    --n_steps 10000 \
    --n_chains 8 \
    --outdir results/mcmc_full/ \
    --parallel_mpi

# Resume interrupted chain
python analysis/run_mcmc.py \
    --resume \
    --chain_dir results/mcmc_full/ \
    --n_steps 5000

# High-resolution production run (cluster)
python analysis/run_mcmc.py \
    --config examples/publication.ini \
    --n_steps 50000 \
    --n_chains 32 \
    --outdir results/mcmc_pub/ \
    --parallel_mpi \
    --verbose
```

**Configuration file (`examples/*.ini`):**

```ini
[general]
# Data to use
use_planck = True
use_act = True
use_spt = False
use_des = True
use_desi = True

# Leakage parameters
kc_min = 0.3            # Prior: min cutoff scale
kc_max = 1.5            # Prior: max cutoff scale
p_min = 1.5             # Prior: min exponent
p_max = 3.5             # Prior: max exponent

# MCMC settings
n_steps = 10000         # Steps per chain
n_burn = 2000           # Burn-in steps
n_chains = 8            # Parallel chains
random_seed = 42

[output]
outdir = results/mcmc/
save_interval = 100     # Save chains every N steps
verbose = True
```

**Command-line arguments:**

```
Configuration:
  --config STR           Config file path (required)
  --mode STR             'sample' or 'test' (default: 'sample')

MCMC settings:
  --n_steps INT          Steps per chain (default: from config)
  --n_chains INT         Parallel chains (default: from config)
  --n_burn INT           Burn-in steps (default: from config)

Data selection:
  --use_planck BOOL      Include Planck data (default: True)
  --use_act BOOL         Include ACT data (default: from config)
  --use_spt BOOL         Include SPT data (default: from config)
  --use_des BOOL         Include DES weak lensing (default: from config)
  --use_desi BOOL        Include DESI Lyman-α (default: from config)

Performance:
  --parallel_mpi BOOL    Use MPI parallelization (default: False)
  --nproc INT            Number of processes (default: 4)
  --resume BOOL          Resume from existing chain (default: False)

Output:
  --outdir STR           Output directory (default: results/mcmc/)
  --verbose BOOL         Verbose output (default: True)
```

**Outputs:**

```
results/mcmc_full/
├── config_used.ini                    # Config file used
├── chains/
│   ├── chain_0_*.txt                  # Chain samples (chain 0)
│   ├── chain_1_*.txt                  # Chain samples (chain 1)
│   └── ...
├── plots/
│   ├── convergence_kc.png             # Trace plot: kc parameter
│   ├── convergence_p.png              # Trace plot: p parameter
│   ├── posterior_1d_kc.png            # Marginal posterior: kc
│   ├── posterior_1d_p.png             # Marginal posterior: p
│   ├── posterior_2d_kc_p.png          # Joint posterior: kc vs p
│   ├── chains_corner_plot.png         # Full corner plot
│   └── gelman_rubin_diagnostic.png    # Convergence statistics
├── statistics/
│   ├── summary_statistics.txt         # Mean, std, credible intervals
│   ├── covariance_matrix.txt          # Parameter covariance
│   ├── correlation_matrix.txt         # Parameter correlations
│   └── gelman_rubin_Rhat.txt          # R̂ < 1.01 (converged?)
├── mcmc_log.txt                       # Execution log
└── best_fit_model.npz                 # Best-fit parameters
```

**Output interpretation:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Load chain samples
chains = np.loadtxt('results/mcmc_full/chains/chain_0_0.txt')
kc_samples = chains[:, 0]  # First column is kc
p_samples = chains[:, 1]   # Second column is p

# Compute posteriors (68% credible interval)
kc_mean = np.mean(kc_samples)
kc_std = np.std(kc_samples)
kc_low, kc_high = np.percentile(kc_samples, [16, 84])

print(f"kc = {kc_mean:.3f} +{kc_high-kc_mean:.3f} -{kc_mean-kc_low:.3f} h/Mpc")

# Check convergence (Gelman-Rubin R̂)
# R̂ < 1.01 = converged
# R̂ > 1.05 = not converged, run longer
```

**Convergence diagnostics:**

```bash
# Check if chains converged
python analysis/check_convergence.py \
    --chain_dir results/mcmc_full/ \
    --plot

# Expected output:
# R̂_kc = 1.002  ✓ (converged)
# R̂_p = 1.003   ✓ (converged)
```

**Performance tips:**

```bash
# Typical runtime estimates:

# Quick test (Planck only, 1000 steps)
--n_steps 1000 --n_chains 4 --use_des False --use_desi False
# ~10 minutes

# Standard run (Planck + ACT + DES, 10000 steps)
--n_steps 10000 --n_chains 8
# ~4–6 hours (single CPU)
# ~30 min (with 16 cores, MPI)

# Publication run (all data, 50000 steps)
--n_steps 50000 --n_chains 32 --parallel_mpi
# ~24 hours (cluster with 100+ cores)
```

---

### **`fisher_forecast.py`** — Fisher Matrix Forecasts

**Purpose:** Predict constraining power on leakage parameters for future surveys.

**Status:** ⏳ **Planned for v1.8.0** (not yet implemented)

**Planned functionality:**

```bash
# CMB-S4 forecast
python analysis/fisher_forecast.py \
    --survey cmb_s4 \
    --lmax 5000 \
    --outdir results/forecast_cmbs4/

# DESI-like Lyman-α forecast
python analysis/fisher_forecast.py \
    --survey desi_extended \
    --kmax 10 \
    --outdir results/forecast_desi/

# Combined forecast (CMB-S4 + DESI extended)
python analysis/fisher_forecast.py \
    --survey combined \
    --outdir results/forecast_combined/
```

**Expected outputs:**
- Fisher matrix eigenvalues/eigenvectors
- Forecast credible intervals on (kc, p)
- Comparison to current constraints

---

## 🔄 Complete Workflow Example

### **Step 1: Validate Leakage Patch**

```bash
# Run validation tests
python validation/test_suppression.py

# Expected output:
# ✓ Transfer function cutoff at k=0.75: OK
# ✓ G_eff suppression: 0.75 ± 0.02
# ✓ Power spectrum modification: OK
# All validation tests passed
```

### **Step 2: Run ΔS8 Sensitivity Scan**

```bash
# Scan to find where model best matches observations
python analysis/compute_delta_S8.py \
    --p 2.0 \
    --nkc 100 \
    --nproc 16 \
    --outdir results/delta_s8_scan/

# Check results
python -c "
import numpy as np
data = np.load('results/delta_s8_scan/delta_s8_summary.npz')
print('ΔS₈ range:', np.min(data['delta_s8']), '-', np.max(data['delta_s8']))
best_idx = np.argmin(np.abs(data['delta_s8'] - 0.025))
print(f'Best-fit kc: {data[\"kc\"][best_idx]:.3f} h/Mpc')
"
```

### **Step 3: Run MCMC to Infer Posterior**

```bash
# Create config for MCMC
cat > examples/analysis_config.ini << EOF
[general]
use_planck = True
use_act = True
use_des = True
use_desi = True
kc_min = 0.3
kc_max = 1.5
p_min = 1.5
p_max = 3.5
n_steps = 20000
n_chains = 8
EOF

# Run MCMC
python analysis/run_mcmc.py \
    --config examples/analysis_config.ini \
    --outdir results/mcmc_joint/ \
    --parallel_mpi \
    --verbose

# Monitor progress (in separate terminal)
tail -f results/mcmc_joint/mcmc_log.txt
```

### **Step 4: Analyze Results**

```bash
# Generate summary statistics
python analysis/summarize_chains.py \
    --chain_dir results/mcmc_joint/ \
    --outdir results/mcmc_joint/analysis/

# Create publication figures
python analysis/make_figures.py \
    --chain_dir results/mcmc_joint/ \
    --figdir results/figures/ \
    --style publication

# Expected figures:
# - Posterior corner plot
# - Tension diagnostics (S₈ vs ΛCDM)
# - Comparison to other models
```

---

## 📈 Input/Output Specifications

### **Input: CAMB Settings**

Scripts expect CAMB with leakage patch applied:

```python
# Standard CAMB parameters
camb_params = {
    'H0': 67.4,              # Hubble constant
    'ombh2': 0.049,          # Baryon density
    'omch2': 0.12,           # Cold dark matter density
    'ns': 0.965,             # Scalar spectral index
    'As': 2.1e-9,            # Primordial amplitude
}

# Leakage parameters (varied in analysis)
leakage_params = {
    'k_cutoff': 0.75,        # Transfer function cutoff (h/Mpc)
    'exponent': 2.0,         # Power-law exponent
}
```

### **Input: Likelihood Data**

Required files in `data/`:

```
data/
├── planck/plc_3.0/          Planck likelihood files
├── act_dr6/                 ACT DR6 data
├── spt3g/                   SPT-3G data
├── weak_lensing/des_year3/  DES Y3 weak lensing
└── lyman_alpha/desi_dr1/    DESI Lyman-α
```

See `data/README.md` for download instructions.

### **Output: Chain Format**

MCMC chains are stored as text files:

```
# Header line (# followed by column names)
# iteration  kc       p        likelihood  posterior

# Data lines (space-separated)
0           0.750    2.000    -5234.2      -5234.3
1           0.752    2.005    -5233.8      -5233.9
2           0.748    1.998    -5235.1      -5235.2
...
```

Load with:
```python
import numpy as np
chains = np.loadtxt('chain_0_0.txt', skiprows=1)
kc_samples = chains[:, 1]
```

---

## 🔧 Troubleshooting

### **Problem: CAMB Import Error**

**Error:**
```
ModuleNotFoundError: No module named 'camb'
```

**Solution:**
```bash
# Reinstall CAMB
pip install --force-reinstall camb

# Test import
python -c "import camb; print(camb.__version__)"
```

---

### **Problem: Likelihood File Not Found**

**Error:**
```
FileNotFoundError: data/planck/plc_3.0/.../plik_rd12_HM_v22_TT.clik
```

**Solution:**
```bash
# Download likelihood data
# See data/README.md

# Verify files exist
ls -la data/planck/plc_3.0/hi_l/*.clik
```

---

### **Problem: MCMC Chain Not Converging**

**Error:**
```
Warning: R̂ > 1.05 for parameter kc (not converged)
```

**Solution:**
```bash
# Increase number of steps
python analysis/run_mcmc.py \
    --resume \
    --chain_dir results/mcmc_full/ \
    --n_steps 10000  # Run 10k more steps

# Or increase burn-in
# Edit config: n_burn = 5000
```

---

### **Problem: Memory Issues**

**Error:**
```
MemoryError: Unable to allocate X.XX GiB
```

**Solution:**
```bash
# Reduce parallel chains
python analysis/run_mcmc.py \
    --config examples/config.ini \
    --n_chains 4  # Reduce from 8

# Or disable certain likelihoods
python analysis/run_mcmc.py \
    --config examples/config.ini \
    --use_desi False  # Skip high-res Lyman-α
```

---

### **Problem: Slow Computation**

**Optimization:**
```bash
# Use parallel processing for ΔS8 scan
python analysis/compute_delta_S8.py \
    --nproc 16  # More processors

# Use MPI for MCMC
python analysis/run_mcmc.py \
    --config examples/config.ini \
    --parallel_mpi

# Reduce resolution
python analysis/compute_delta_S8.py \
    --nkc 50  # Fewer points
    --camb_acc 2  # Lower CAMB accuracy
```

---

## 📚 Advanced Usage

### **Custom Parameter Priors**

Edit config file to set custom priors:

```ini
[priors]
# Uniform priors
kc_min = 0.3
kc_max = 1.5

# Gaussian prior (optional)
p_mean = 2.0
p_sigma = 0.5
```

### **Comparing Models**

Run MCMC for multiple models and compare:

```bash
# ΛCDM only
python analysis/run_mcmc.py \
    --config examples/lambda_cdm.ini \
    --outdir results/mcmc_lambda_cdm/

# Leakage model
python analysis/run_mcmc.py \
    --config examples/leakage.ini \
    --outdir results/mcmc_leakage/

# Compare using Bayesian evidence
python analysis/compare_models.py \
    --model1 results/mcmc_lambda_cdm/ \
    --model2 results/mcmc_leakage/
```

---

## 📞 Questions & Support

**For script issues:**
- Check the script docstring: `python analysis/compute_delta_S8.py --help`
- Run with `--verbose` for debugging output
- Check log files in output directory

**For analysis questions:**
- Email: geometriccosmo.illusion559@passinbox.com
- GitHub Issues: Use `analysis` label

---

**Last updated:** June 2026  
**Maintained by:** Sparky (GeometricCosmo)  
**Version:** 1.0
