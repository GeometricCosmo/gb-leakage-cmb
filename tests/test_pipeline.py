# Path: tests/test_pipeline.py
"""
End-to-end pipeline test for gb-leakage-cmb.
Checks that leakage patch, validation, and plotting scripts run without errors
and produce expected output files.
"""

import os
import subprocess

def run_cmd(cmd, expected_output=None):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {cmd}")
    if expected_output and not os.path.exists(expected_output):
        raise FileNotFoundError(f"Expected output not found: {expected_output}")
    print(f"✓ Success: {cmd}")

def main():
    # Ensure directories exist
    os.makedirs("figures", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    # 1. Validation test
    run_cmd("python validation/test_suppression.py")

    # 2. Analytic envelope plot
    run_cmd("python notebooks/validation_quick.py", "figures/validation_quick.png")

    # 3. Transfer function plot
    run_cmd("python plots/plot_transfer.py", "figures/transfer_function.png")

    # 4. Residual ratio plot
    run_cmd("python plots/plot_residuals.py", "figures/tt_residual_ratio.png")

    # 5. ΔS8 scan
    run_cmd("python analysis/compute_delta_S8.py --p 2.0 --nproc 2 --outdir results",
            "results/delta_s8_summary.npz")

    # 6. Corner plot (synthetic data if no chains)
    run_cmd("python plots/plot_corner.py", "figures/corner_kc_p.png")

    print("\nAll pipeline tests completed successfully.")

if __name__ == "__main__":
    main()
