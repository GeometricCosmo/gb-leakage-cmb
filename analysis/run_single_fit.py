# Path: analysis/run_single_fit.py
"""
Thin wrapper that selects an engine (CosmoMC/MontePython) and prepares runs
with (kc, p) and foreground strategy. Replace placeholders with your engine calls.
"""
import argparse
import subprocess
from pathlib import Path

def prepare_config(engine, kc, p, foreground, outdir, seed):
    Path(outdir).mkdir(parents=True, exist_ok=True)

    if engine.lower() == "cosmomc":
        # Example: call a wrapper that writes CosmoMC .ini files
        cmd = [
            "python", "-m", "cosmomc_wrapper",
            "--kc", str(kc), "--p", str(p),
            "--foreground", foreground,
            "--seed", str(seed),
            "--outdir", outdir
        ]
    elif engine.lower() == "montepython":
        # Example: call a wrapper that writes MontePython .param files
        cmd = [
            "python", "-m", "montepython_wrapper",
            "--kc", str(kc), "--p", str(p),
            "--foreground", foreground,
            "--seed", str(seed),
            "--outdir", outdir
        ]
    else:
        raise ValueError(f"Unknown engine: {engine}")

    return cmd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", type=str, default="cosmomc", choices=["cosmomc", "montepython"])
    ap.add_argument("--kc", type=float, required=True)
    ap.add_argument("--p", type=float, required=True)
    ap.add_argument("--foreground", type=str, default="baseline", choices=["baseline", "conservative", "minimal"])
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--outdir", type=str, default="chains")
    ap.add_argument("--nprocs", type=int, default=4)
    args = ap.parse_args()

    cmd = prepare_config(args.engine, args.kc, args.p, args.foreground, args.outdir, args.seed)
    print("Launching:", " ".join(cmd))
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
