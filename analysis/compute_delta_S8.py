# Path: analysis/compute_delta_S8.py
"""
Scan over kc values and compute the shift in S8 due to leakage suppression.
Saves results to a .npz file and produces a plot.
"""
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from multiprocessing import Pool
import camb
from src.camb_leakage_patch import make_Pmod_table

def sigma8_worker(kc, p, kh, As, ns):
    # Build modified spectrum
    _, P_mod = make_Pmod_table(kh, As=As, ns=ns, kc=kc, p=p)

    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120,
                       mnu=0.06, omk=0, tau=0.054)
    pars.set_for_lmax(2500)

    try:
        pars.set_initial_power_table(kh, P_mod)
    except Exception:
        pars.InitPower.set_custom_power_spectrum(kh, P_mod)

    results = camb.get_results(pars)
    sigma8 = results.get_sigma8()
    omegam = pars.omegam
    S8 = sigma8 * (omegam / 0.3) ** 0.5
    return kc, S8

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nproc", type=int, default=4,
                    help="Number of parallel processes")
    ap.add_argument("--p", type=float, default=2.0,
                    help="Exponent p in transfer function")
    ap.add_argument("--outdir", type=str, default="results",
                    help="Output directory")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # Dense k grid
    kh = np.logspace(-4, 1.5, 3000)
    As = 2.1e-9
    ns = 0.965

    # Baseline (no suppression)
    _, S8_base = sigma8_worker(1e6, args.p, kh, As, ns)

    kc_vals = np.linspace(0.1, 2.0, 40)
    worker = partial(sigma8_worker, p=args.p, kh=kh, As=As, ns=ns)

    with Pool(processes=args.nproc) as pool:
        results = pool.map(worker, kc_vals)

    results.sort(key=lambda x: x[0])
    kc_res = np.array([r[0] for r in results])
    S8_res = np.array([r[1] for r in results])
    delta_S8 = S8_res - S8_base

    # Save numerical results
    np.savez(os.path.join(args.outdir, "delta_s8_summary.npz"),
             kc=kc_res, S8=S8_res, delta_S8=delta_S8, S8_base=S8_base)

    # Plot
    plt.figure(figsize=(6,4))
    plt.plot(kc_res, delta_S8, 'o-', color='navy',
             label=f'GB Model (p={args.p})')
    plt.axhline(0, color='gray', linestyle='--')
    plt.xlabel(r'$k_c$ [Mpc$^{-1}$]')
    plt.ylabel(r'$\Delta S_8$')
    plt.title(f'S8 Alleviation (p={args.p})')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    outpath = os.path.join(args.outdir, 'delta_S8_vs_kc.png')
    plt.savefig(outpath, dpi=300)
    print(f"Saved: {outpath}")

if __name__ == "__main__":
    main()
