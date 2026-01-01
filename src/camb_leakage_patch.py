"""
Injects P_mod(k) = P_prim(k) * T(k)^2 into CAMB via a dense log-k table.
Exposes: T_of_k, make_Pmod_table, compute_leakage_cl
"""
import numpy as np
import camb

def T_of_k(k, kc=0.75, p=2.5):
    return np.exp(- (k / kc) ** p)

def make_Pmod_table(kh, As=2.1e-9, ns=0.965, kc=0.75, p=2.5, pivot=0.05):
    P_prim = As * (kh / pivot) ** (ns - 1.0)
    T_k = T_of_k(kh, kc, p)
    P_mod = P_prim * T_k ** 2
    return kh, P_mod

def compute_leakage_cl(kc=0.75, p=2.5, lmax=5000, As=2.1e-9, ns=0.965):
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.4, ombh2=0.0224, omch2=0.120, mnu=0.06, omk=0, tau=0.054)
    pars.InitPower.set_params(As=As, ns=ns)
    pars.set_for_lmax(lmax)

    kh = np.logspace(-4, 1.5, 3000)
    kh_table, P_mod = make_Pmod_table(kh, As=As, ns=ns, kc=kc, p=p)

    try:
        pars.set_initial_power_table(kh_table, P_mod)
    except Exception:
        try:
            pars.InitPower.set_custom_power_spectrum(kh_table, P_mod)
        except Exception:
            raise RuntimeError("CAMB version does not support custom power table.")

    results = camb.get_results(pars)
    spectra = results.get_cmb_power_spectra(pars, lmax=lmax)
    cls_tt = spectra['total'][:, 0]
    ells = np.arange(len(cls_tt))
    return ells, cls_tt, results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--kc", type=float, default=0.75)
    parser.add_argument("--p", type=float, default=2.5)
    parser.add_argument("--ell", type=int, default=3000)
    args = parser.parse_args()

    chi_rec = 13800.0
    k = args.ell / chi_rec
    analytic_supp = 100.0 * (1.0 - T_of_k(k, args.kc, args.p) ** 2)

    ells, cls_mod, _ = compute_leakage_cl(kc=args.kc, p=args.p, lmax=max(args.ell, 3000))
    ells_b, cls_base, _ = compute_leakage_cl(kc=1e6, p=args.p, lmax=max(args.ell, 3000))
    cam_supp = 100.0 * (1.0 - cls_mod[args.ell] / cls_base[args.ell])

    print(f"Analytic suppression at ell={args.ell}: {analytic_supp:.2f}%")
    print(f"CAMB suppression at ell={args.ell}: {cam_supp:.2f}%")
