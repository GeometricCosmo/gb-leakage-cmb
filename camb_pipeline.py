"""
CAMB pipeline for GB leakage model with full validation and comparison tools.

This module provides a configurable GB leakage model, custom primordial power
spectrum injection into CAMB, baseline comparisons, validation diagnostics, and
plotting support.
"""

import warnings

import numpy as np
import camb


class GBLeakageModel:
    """Modified gravity model with exponential transfer function."""

    def __init__(self, kc=0.75, p=2.5, As=2.1e-9, ns=0.965, pivot=0.05):
        self.kc = float(kc)
        self.p = float(p)
        self.As = float(As)
        self.ns = float(ns)
        self.pivot = float(pivot)

    def transfer_function(self, k):
        """T(k) = exp(-(k/kc)^p)."""
        return np.exp(-np.power(k / self.kc, self.p))

    def primordial_power(self, k):
        """P_prim(k) = A_s * (k/pivot)^(n_s - 1)."""
        return self.As * np.power(k / self.pivot, self.ns - 1.0)

    def modified_power(self, k):
        """P_mod(k) = P_prim(k) * T(k)^2."""
        return self.primordial_power(k) * np.square(self.transfer_function(k))

    def suppression_factor(self, k):
        """Fractional suppression relative to baseline: 1 - T(k)^2."""
        T = self.transfer_function(k)
        return 1.0 - np.square(T)


def _ensure_k_grid(kh, k_min=-4, k_max=1.5):
    if kh[0] > 10**k_min or kh[-1] < 10**k_max:
        warnings.warn(
            f"Provided k grid [{kh[0]:.2g}, {kh[-1]:.2g}] does not cover the expected "
            f"range [1e{k_min}, 1e{k_max}] for the GB leakage transfer function.")


def _inject_power_table(pars, kh, P_mod):
    try:
        pars.set_initial_power_table(kh, P_mod)
    except Exception as e1:
        try:
            pars.InitPower.set_custom_power_spectrum(kh, P_mod)
        except Exception as e2:
            raise RuntimeError(
                "Failed to inject custom power table into CAMB. "
                f"Error 1: {e1}. Error 2: {e2}.")


def compute_camb_results(
    model,
    lmax=5000,
    H0=67.4,
    ombh2=0.0224,
    omch2=0.120,
    mnu=0.06,
    omk=0,
    tau=0.054,
    kmin=-4,
    kmax=1.5,
    nk=3000,
    return_spectra=True,
    return_transfer=True,
):
    """Run CAMB with modified power spectrum from a GB leakage model."""
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, mnu=mnu, omk=omk, tau=tau)
    pars.InitPower.set_params(As=model.As, ns=model.ns)
    pars.set_for_lmax(lmax)

    kh = np.logspace(kmin, kmax, nk)
    _ensure_k_grid(kh, kmin, kmax)

    P_mod = model.modified_power(kh)
    _inject_power_table(pars, kh, P_mod)

    results = camb.get_results(pars)
    output = {
        'results': results,
        'model': model,
        'k_grid': kh,
        'P_mod': P_mod,
        'lmax': lmax,
    }

    if return_spectra:
        spectra = results.get_cmb_power_spectra(pars, lmax=lmax)
        ells = np.arange(spectra['total'].shape[0])
        output['ells'] = ells
        output['cls_tt'] = spectra['total'][:, 0]
        output['cls_ee'] = spectra['total'][:, 1] if spectra['total'].shape[1] > 1 else None
        output['cls_te'] = spectra['total'][:, 3] if spectra['total'].shape[1] > 3 else None
        output['cls_bb'] = spectra['total'][:, 2] if spectra['total'].shape[1] > 2 else None

    if return_transfer:
        try:
            transfer_data = results.get_matter_transfer_data()
            output['k_transfer'] = np.array(transfer_data.k)
            output['transfer_m'] = np.array(transfer_data.transfer_m[:, 0])
        except Exception:
            output['k_transfer'] = None
            output['transfer_m'] = None

    return output


def compare_models(models_dict, cosmology_dict=None, lmax=5000):
    """Compute CAMB results for a set of GB leakage models."""
    if cosmology_dict is None:
        cosmology_dict = {
            'H0': 67.4,
            'ombh2': 0.0224,
            'omch2': 0.120,
            'mnu': 0.06,
            'omk': 0,
            'tau': 0.054,
        }

    results = {}
    for name, model in models_dict.items():
        print(f"Running model: {name}")
        results[name] = compute_camb_results(
            model,
            lmax=lmax,
            H0=cosmology_dict['H0'],
            ombh2=cosmology_dict['ombh2'],
            omch2=cosmology_dict['omch2'],
            mnu=cosmology_dict['mnu'],
            omk=cosmology_dict['omk'],
            tau=cosmology_dict['tau'],
        )
    return results


def validate_transfer_function(model, lmax=3000, chi_rec=13800.0):
    """Validate CAMB suppression against the analytic transfer function."""
    if model.kc <= 0:
        raise ValueError("kc must be positive for validation.")

    results_mod = compute_camb_results(model, lmax=lmax)
    baseline = GBLeakageModel(kc=1e6, p=model.p, As=model.As, ns=model.ns)
    results_base = compute_camb_results(baseline, lmax=lmax)

    ells = results_mod['ells']
    cls_mod = results_mod['cls_tt']
    cls_base = results_base['cls_tt']

    suppression_camb = np.full_like(cls_mod, np.nan)
    valid = cls_base > 0
    suppression_camb[valid] = 1.0 - (cls_mod[valid] / cls_base[valid])

    k_eff = ells / chi_rec
    suppression_analytic = model.suppression_factor(k_eff)

    relative_error = np.full_like(suppression_analytic, np.nan)
    nonzero = np.abs(suppression_analytic) > 0
    relative_error[nonzero] = np.abs(
        suppression_analytic[nonzero] - suppression_camb[nonzero]) / np.abs(suppression_analytic[nonzero])

    diagnostics = {
        'ells': ells,
        'suppression_analytic': suppression_analytic,
        'suppression_camb': suppression_camb,
        'relative_error': relative_error,
    }

    return diagnostics


def plot_results(results, output_path=None):
    """Plot transfer function, power modification, and TT spectrum diagnostics."""
    import matplotlib.pyplot as plt

    model = results['model']
    ells = results['ells']
    cls_tt = results['cls_tt']

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    k_plot = np.logspace(-2, 1, 500)
    T_k = model.transfer_function(k_plot)
    axes[0, 0].loglog(k_plot, T_k)
    axes[0, 0].set_xlabel('k [Mpc$^{-1}$]')
    axes[0, 0].set_ylabel('T(k)')
    axes[0, 0].set_title('GB Leakage Transfer Function')
    axes[0, 0].grid(True)

    P_prim = model.primordial_power(k_plot)
    P_mod = model.modified_power(k_plot)
    axes[0, 1].loglog(k_plot, P_mod / P_prim)
    axes[0, 1].set_xlabel('k [Mpc$^{-1}$]')
    axes[0, 1].set_ylabel('P_mod / P_prim')
    axes[0, 1].set_title('Primordial Spectrum Modification')
    axes[0, 1].grid(True)

    D_ell = ells * (ells + 1) * cls_tt / (2.0 * np.pi)
    axes[1, 0].plot(ells, D_ell)
    axes[1, 0].set_xlim(0, min(3000, ells.max()))
    axes[1, 0].set_xlabel('ℓ')
    axes[1, 0].set_ylabel('D_ℓ^{TT} [μK^2]')
    axes[1, 0].set_title('CMB TT Power Spectrum')
    axes[1, 0].grid(True)

    if 'suppression_analytic' in results:
        axes[1, 1].semilogy(ells, results['suppression_analytic'], label='Analytic')
        axes[1, 1].semilogy(ells, results['suppression_camb'], label='CAMB', linestyle='--')
        axes[1, 1].set_xlabel('ℓ')
        axes[1, 1].set_ylabel('Suppression')
        axes[1, 1].set_title('Suppression Validation')
        axes[1, 1].legend()
        axes[1, 1].grid(True)
    else:
        axes[1, 1].axis('off')

    plt.tight_layout()

    if output_path is not None:
        fig.savefig(output_path, dpi=150)
        print(f"Saved plot to {output_path}")
    else:
        plt.show()

    plt.close(fig)


def _summary_line(kc, p):
    return f"kc={kc:.3f}, p={p:.2f}"


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='GB Leakage CAMB Pipeline')
    parser.add_argument('--kc', type=float, default=0.75, help='Cutoff wavenumber [Mpc^-1]')
    parser.add_argument('--p', type=float, default=2.5, help='Transfer exponent')
    parser.add_argument('--lmax', type=int, default=3000, help='Maximum multipole')
    parser.add_argument('--validate', action='store_true', help='Run analytic validation')
    parser.add_argument('--plot', action='store_true', help='Produce summary plots')
    parser.add_argument('--output', type=str, default=None, help='Output plot filename')
    args = parser.parse_args()

    model = GBLeakageModel(kc=args.kc, p=args.p)
    results = compute_camb_results(model, lmax=args.lmax)

    print('✓ CAMB computation complete')
    print(f"  - {len(results['ells'])} multipoles computed")
    print(f"  - model: { _summary_line(args.kc, args.p) }")

    if args.validate:
        diag = validate_transfer_function(model, lmax=args.lmax)
        results.update(diag)
        print('✓ Validation complete')
        test_ells = sorted(set([100, 500, 1000, 2000, min(3000, args.lmax)]))
        for ell in test_ells:
            if ell < len(diag['ells']):
                print(
                    f"ell={ell:4d}  analytic={100.0 * diag['suppression_analytic'][ell]:6.2f}% "
                    f"CAMB={100.0 * diag['suppression_camb'][ell]:6.2f}% "
                    f"rel_err={diag['relative_error'][ell]:.3f}")

    if args.plot:
        output_path = args.output or 'gb_leakage_camb_summary.png'
        plot_results(results, output_path=output_path)
