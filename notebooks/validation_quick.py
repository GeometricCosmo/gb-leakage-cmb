# Path: notebooks/validation_quick.py
import numpy as np
import matplotlib.pyplot as plt
from src.camb_leakage_patch import T_of_k
import os

def main():
    # Example parameters
    kc, p = 0.75, 2.5
    chi_rec = 13800.0  # comoving distance to recombination (Mpc)

    # Multipole range
    ell = np.linspace(1000, 4000, 500)
    k = ell / chi_rec
    Tk2 = T_of_k(k, kc, p)**2

    # Ensure output directory exists
    os.makedirs('figures', exist_ok=True)

    # Plot analytic suppression envelope
    plt.figure(figsize=(7,4))
    plt.plot(ell, Tk2, 'r-', lw=2, label=r'$T(k)^2$ envelope')
    plt.axvline(3000, color='gray', ls='--', alpha=0.5)
    plt.xlabel(r'$\ell$')
    plt.ylabel(r'$T(k)^2$')
    plt.title('Analytic suppression envelope vs multipole')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    outpath = 'figures/validation_quick.png'
    plt.savefig(outpath, dpi=300)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    main()
