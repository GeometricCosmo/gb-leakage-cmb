# Path: plots/plot_transfer.py
import numpy as np
import matplotlib.pyplot as plt
from src.camb_leakage_patch import T_of_k
import os

def main():
    # Example parameters
    kc, p = 0.75, 2.5
    k = np.linspace(0.01, 1.5, 500)
    Tk = T_of_k(k, kc, p)

    # Ensure output directory exists
    os.makedirs('figures', exist_ok=True)

    # Plot transfer function
    plt.figure(figsize=(6,4))
    plt.plot(k, Tk, 'r-', lw=2)
    plt.xlabel(r'$k$ [Mpc$^{-1}$]')
    plt.ylabel(r'$T(k)$')
    plt.title(f'Transfer function T(k), kc={kc}, p={p}')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    outpath = 'figures/transfer_function.png'
    plt.savefig(outpath, dpi=300)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    main()
