# Path: plots/plot_residuals.py
import numpy as np
import matplotlib.pyplot as plt
from src.camb_leakage_patch import compute_leakage_cl
import os

def main():
    # Example parameters
    kc, p = 0.75, 2.5
    lmax = 4000

    # Compute spectra with leakage
    ells, cls_mod, _ = compute_leakage_cl(kc=kc, p=p, lmax=lmax)
    # Baseline (no suppression)
    ells_b, cls_base, _ = compute_leakage_cl(kc=1e6, p=p, lmax=lmax)

    # Ratio of modified to baseline
    ratio = cls_mod / cls_base

    # Ensure output directory exists
    os.makedirs('figures', exist_ok=True)

    # Plot residual ratio
    plt.figure(figsize=(7,4))
    plt.plot(ells[:lmax], ratio[:lmax], 'g-', lw=1.5)
    plt.axhline(1.0, color='k', ls='--', alpha=0.5)
    plt.xlim(1500, lmax)
    plt.ylim(0.85, 1.05)
    plt.xlabel(r'$\ell$')
    plt.ylabel(r'$C_\ell^{\rm mod}/C_\ell^{\Lambda{\rm CDM}}$')
    plt.title('TT residual ratio (model vs baseline)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    outpath = 'figures/tt_residual_ratio.png'
    plt.savefig(outpath, dpi=300)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    main()
