# Comparison to Related Cosmology Repositories

This document situates **gb-leakage-cmb** within the broader landscape of cosmology software.

---

## CLASS (Cosmic Linear Anisotropy Solving System)
- **Repo**: https://github.com/lesgourg/class_public  
- **Scope**: General-purpose Boltzmann solver for CMB anisotropies, matter transfer functions, background evolution.  
- **Popularity**: ~280 stars, 340 forks (as of late 2025).  
- **Relation to gb-leakage-cmb**:  
  CLASS is the backbone solver. Our repo acts as a *mod* or extension, injecting a Gauss–Bonnet leakage ansatz into the primordial spectrum. CLASS is broad; ours is focused on one phenomenological model.

---

## CAMB (Code for Anisotropies in the Microwave Background)
- **Repo**: https://github.com/cmbant/CAMB  
- **Scope**: Computes CMB power spectra, lensing, matter power, transfer functions.  
- **Popularity**: ~230 stars, 180 forks.  
- **Relation to gb-leakage-cmb**:  
  CAMB is an alternative engine to CLASS. Our repo demonstrates how to patch CAMB for leakage suppression. CAMB is optimized for precision; ours is narrower but complements it by showing how to hack in custom damping.

---

## MontePython
- **Repo**: https://github.com/brinckmann/montepython_public  
- **Scope**: MCMC sampler for cosmological parameter estimation, integrated with CLASS.  
- **Popularity**: ~100 stars, 90 forks.  
- **Relation to gb-leakage-cmb**:  
  MontePython provides the fitting framework. Our `analysis/` directory shows how to extend it with leakage parameters \((k_c, p)\). Together they enable posterior inference on high‑ℓ suppression.

---

## HiCLASS (Horndeski in CLASS)
- **Repo**: https://github.com/mishakb/hi_class_public  
- **Scope**: Modified CLASS for Horndeski gravity models.  
- **Popularity**: ~20 stars.  
- **Relation to gb-leakage-cmb**:  
  HiCLASS is a peer project: both repos patch CLASS for modified gravity phenomenology. HiCLASS focuses on scalar fields; ours focuses on Gauss–Bonnet leakage. Both demonstrate how to extend CLASS for new physics.

---

## Summary

### Strengths of gb-leakage-cmb
- Hyper‑focused on reproducibility for one model.  
- Clean structure (`src/`, `analysis/`, `plots/`, `validation/`).  
- Easy to replicate paper figures.  

### Weaknesses vs. others
- New repo (low visibility).  
- Narrow scope (one model vs. general frameworks).  

### Positioning
gb-leakage-cmb is an **application‑layer extension** of CLASS/CAMB, similar in spirit to HiCLASS.  
It fills a niche for high‑ℓ CMB phenomenology and provides reproducible pipelines for immediate paper replication.

---
