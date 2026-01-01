# Path: analysis/run_mcmc.py
"""
Convenience launcher for local runs. Delegates to run_single_fit.py.
"""
import argparse
import subprocess

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", type=str, default="cosmomc", choices=["cosmomc", "montepython"])
    ap.add_argument("--kc", type=float, default=0.75)
    ap.add_argument("--p", type=float, default=2.5)
    ap.add_argument("--foreground", type=str, default="baseline", choices=["baseline", "conservative", "minimal"])
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--outdir", type=str, default="chains")
    ap.add_argument("--nprocs", type=int, default=4)
    args = ap.parse_args()

    cmd = [
        "python", "analysis/run_single_fit.py",
        "--engine", args.engine,
        "--kc", str(args.kc),
        "--p", str(args.p),
        "--foreground", args.foreground,
        "--seed", str(args.seed),
        "--outdir", args.outdir,
        "--nprocs", str(args.nprocs)
    ]
    print("Launching:", " ".join(cmd))
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
