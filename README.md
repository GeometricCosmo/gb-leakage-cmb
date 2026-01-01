# gb-leakage-cmb
Phenomenological Gauss–Bonnet braneworld leakage model for high‑ℓ CMB suppression. Includes CAMB/CLASS patches, MCMC scripts, and reproducible pipelines for Planck, ACT DR6, and SPT‑3G data.
# Path: README.md
# GB Leakage Model for High-ℓ CMB Suppression

This repository provides a reproducible pipeline to test a phenomenological,
Gauss–Bonnet–inspired leakage model for high-ℓ CMB power suppression.

## Contents
- `src/` : CAMB/CLASS patches implementing P_mod(k) = P_prim(k) * T(k)^2
- `analysis/` : MCMC driver wrappers, ΔS8 scans, Fisher forecast utilities
- `plots/` : plotting utilities for transfer, residuals, and corner plots
- `validation/` : unit tests validating suppression behavior
- `cluster/` : SLURM array script for large parameter scans
- `data/` : helper script to document/download public likelihoods
- `docs/` : theory notes and assumptions

## Quickstart
1. Clone:
   ```bash
   git clone https://github.com/GeometricCosmo/gb-leakage-cmb.git
   cd gb-leakage-cmb
