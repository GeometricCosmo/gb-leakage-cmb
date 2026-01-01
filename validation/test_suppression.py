# Path: validation/test_suppression.py
import unittest
import numpy as np
from src.camb_leakage_patch import compute_leakage_cl, T_of_k

class TestLeakageSuppression(unittest.TestCase):
    def test_ell_3000_suppression(self):
        # Parameters for the test
        kc, p = 0.75, 2.5
        ell = 3000
        chi_rec = 13800.0  # comoving distance to recombination (Mpc)
        k = ell / chi_rec

        # Analytic suppression estimate
        analytic = 100.0 * (1.0 - T_of_k(k, kc, p) ** 2)

        # CAMB run with leakage
        ells, cls_mod, _ = compute_leakage_cl(kc=kc, p=p, lmax=ell)
        # Baseline run (very large kc → no suppression)
        ells_b, cls_base, _ = compute_leakage_cl(kc=1e6, p=p, lmax=ell)

        cam_supp = 100.0 * (1.0 - cls_mod[ell] / cls_base[ell])

        # Allow modest tolerance because CAMB integrates transfer functions
        # over the line of sight, smoothing features slightly.
        self.assertAlmostEqual(cam_supp, analytic, delta=1.0)

if __name__ == "__main__":
    unittest.main()
