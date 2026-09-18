#!/usr/bin/env python3
"""
verify_baseline.py
Independent re-derivation of the v2.0 Layer-1 baseline numbers.

Runs CAMB with Planck 2018 TT,TE,EE+lowE+lensing best-fit parameters,
fixed A_s (no free rescaling), applies the frozen broken-power-law T(k),
and recomputes sigma_8, S_8 and the Lyman-alpha ratio.
"""
import numpy as np
import camb
from scipy.integrate import simpson
import json, os

OUT = os.environ.get("OUTDIR", "/home/claude/work")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- parameters
# Planck 2018 TT,TE,EE+lowE+lensing best fit (Aghanim et al. 2020, Table 1/2)
P18 = dict(H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, omk=0.0,
           tau=0.0544, As=2.100e-9, ns=0.9649)

KC   = 1.5   # break scale, h/Mpc  (FROZEN)
SLP  = 0.5   # power-law index     (FROZEN)
R8   = 8.0   # top-hat radius, Mpc/h

def T_frozen(k_h):
    """Frozen broken power law. k in h/Mpc."""
    return np.where(k_h < KC, 1.0, (KC / k_h) ** SLP)

def W_th(x):
    """Real-space top-hat window in Fourier space."""
    return 3.0 * (np.sin(x) - x * np.cos(x)) / x**3

# ---------------------------------------------------------------- CAMB run
pars = camb.set_params(**P18)
pars.set_matter_power(redshifts=[0.0], kmax=200.0)
pars.NonLinear = camb.model.NonLinear_none
res = camb.get_results(pars)

kh, z, pk = res.get_matter_power_spectrum(minkh=1e-4, maxkh=100.0, npoints=4000)
pk = pk[0]                     # z = 0, linear, units (Mpc/h)^3
om = res.get_Omega('cdm') + res.get_Omega('baryon') + res.get_Omega('nu')
s8_camb = res.get_sigma8_0()

# ---------------------------------------------------------------- sigma_8
def sigma_R(kh, pk, R):
    x = kh * R
    integ = pk * (kh**2) * W_th(x)**2 / (2.0 * np.pi**2)
    return np.sqrt(simpson(integ, x=kh))

s8_lcdm = sigma_R(kh, pk, R8)

# The transfer function multiplies delta, so P -> T^2 P  (convention A, standard)
pk_A = pk * T_frozen(kh)**2
s8_A = sigma_R(kh, pk_A, R8)

# Convention B: T applied directly to P (non-standard; reproduces the old number)
pk_B = pk * T_frozen(kh)
s8_B = sigma_R(kh, pk_B, R8)

S8 = lambda s8: s8 * np.sqrt(om / 0.3)

# ------------------------------------------- where does sigma_8 come from?
x = kh * R8
dsig2 = pk * kh**3 * W_th(x)**2 / (2.0 * np.pi**2)   # d sigma^2 / d ln k
tot = simpson(dsig2 / kh, x=kh)
above = simpson((dsig2 / kh)[kh >= KC], x=kh[kh >= KC])
frac_above = above / tot

# ------------------------------------------------------- Lyman-alpha ratio
ks_old = np.array([0.5, 1.0, 2.0, 3.0])          # the four points used before
ks_lya = np.array([1.0, 2.0, 3.0, 5.0, 8.0, 10.0])  # genuinely Lya-sensitive
rA_old = np.interp(ks_old, kh, pk_A) / np.interp(ks_old, kh, pk)
rB_old = np.interp(ks_old, kh, pk_B) / np.interp(ks_old, kh, pk)
rA_lya = np.interp(ks_lya, kh, pk_A) / np.interp(ks_lya, kh, pk)

# --------------------------------------------------------------- reporting
out = {
    "planck2018_params": P18,
    "Omega_m": float(om),
    "sigma8_camb_internal": float(s8_camb),
    "sigma8_LCDM_quadrature": float(s8_lcdm),
    "S8_LCDM": float(S8(s8_lcdm)),
    "convention_A_P_eq_T2P": {
        "sigma8": float(s8_A), "S8": float(S8(s8_A)),
        "frac_change_sigma8": float(s8_A / s8_lcdm - 1),
        "lya_ratio_old_4pts": float(np.mean(rA_old)),
        "lya_ratios_old_4pts": rA_old.tolist(),
        "lya_ratios_1to10": dict(zip(ks_lya.astype(str), rA_lya.round(4).tolist())),
    },
    "convention_B_P_eq_TP": {
        "sigma8": float(s8_B), "S8": float(S8(s8_B)),
        "frac_change_sigma8": float(s8_B / s8_lcdm - 1),
        "lya_ratio_old_4pts": float(np.mean(rB_old)),
        "lya_ratios_old_4pts": rB_old.tolist(),
    },
    "sigma8_window_weight_above_kc": float(frac_above),
    "S8_over_sigma8_ratio": float(np.sqrt(om / 0.3)),
}

print(json.dumps(out, indent=2))
with open(f"{OUT}/baseline_verification.json", "w") as f:
    json.dump(out, f, indent=2)

np.savetxt(f"{OUT}/pk_baseline.csv",
           np.column_stack([kh, pk, pk_A, pk_B, T_frozen(kh), dsig2]),
           delimiter=",", header="k_hMpc,P_LCDM,P_convA,P_convB,T_k,dsigma2_dlnk",
           comments="")
print("\nwrote", f"{OUT}/baseline_verification.json")
