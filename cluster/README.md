# Cluster / SLURM Scripts for gb-leakage-cmb

This directory contains scripts to run large parameter scans of the Gauss–Bonnet leakage model on HPC clusters using SLURM.

---

## 📂 Scripts

### `slurm_run_fits.sh`
- **Purpose**: Submit an array of MCMC jobs across different leakage parameters \((k_c, p)\).
- **Usage**:
  ```bash
  sbatch cluster/slurm_run_fits.sh
  ```
- **Behavior**:
  - Launches multiple fits in parallel using SLURM job arrays.
  - Each job runs `analysis/run_mcmc.py` with different parameter seeds.
  - Results are saved in `chains/` and `results/`.

---

## 🧩 Workflow

1. Prepare likelihood data in `data/` (see `data/README.md`).
2. Ensure CAMB and MontePython/CosmoMC are installed on the cluster.
3. Edit `slurm_run_fits.sh` to set:
   - Number of jobs (`#SBATCH --array=0-99`)
   - CPUs per task (`#SBATCH --cpus-per-task=8`)
   - Output directories (`chains/`, `results/`)
4. Submit job array:
   ```bash
   sbatch cluster/slurm_run_fits.sh
   ```
5. Monitor progress:
   ```bash
   squeue -u $USER
   tail -f slurm_logs/slurm-<jobid>.out
   ```

---

## 📌 Notes
- Adjust resource requests (`--time`, `--mem`, `--cpus-per-task`) based on cluster limits.
- Outputs are reproducible but may take hours to days depending on chain length.
- For toy runs, use fewer steps locally (`analysis/run_mcmc.py`) before scaling to cluster.

---
