# Path: plots/plot_corner.py
import numpy as np
import corner
import os

def main():
    # Placeholder: load samples from your MCMC chains.
    # For demonstration, we generate synthetic samples around (0.75, 2.5).
    rng = np.random.default_rng(42)
    kc = rng.normal(0.75, 0.15, size=5000)
    p = rng.normal(2.5, 0.5, size=5000)
    data = np.vstack([kc, p]).T

    # Ensure output directory exists
    os.makedirs('figures', exist_ok=True)

    # Generate corner plot
    fig = corner.corner(
        data,
        labels=[r'$k_c$ [Mpc$^{-1}$]', r'$p$'],
        range=[(0.1, 1.5), (1.0, 4.0)],
        color='navy',
        bins=40
    )

    outpath = 'figures/corner_kc_p.png'
    fig.savefig(outpath, dpi=300)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    main()
