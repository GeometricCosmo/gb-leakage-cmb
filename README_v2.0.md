# Radion Leakage in a 5D Gauss-Bonnet Braneworld

**Version 2.0 — negative result. The observational claims of v1.8.x and v1.9.x are retracted.**

[![Version](https://img.shields.io/badge/version-2.0.0-blue)]()
[![Status](https://img.shields.io/badge/result-negative-red)]()
[![Baseline](https://img.shields.io/badge/Layer%201-retracted-red)]()
[![Mechanism](https://img.shields.io/badge/Layer%202-falsified-red)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

**[Paper (PDF)](./v2.0/radion_leakage_v2.0.pdf) · [Locked baseline](./v2.0/V2.0_BASELINE_LOCKED.md) · [Zenodo v1.9.1](https://zenodo.org/records/21663023)**

---

## What this repository now says

A broken power-law transfer function

```
T(k) = 1              for k <  1.5 h/Mpc
T(k) = (1.5/k)^0.5    for k >= 1.5 h/Mpc
```

was previously reported to satisfy S8 and Lyman-alpha constraints simultaneously
while leaving sigma8 too high, and was attributed to a radion in a 5D
Gauss-Bonnet braneworld.

**Independent verification shows that neither the observational claim nor the
attribution survives.** Details are in the v2.0 paper. The short version:

| Claim | Status | Why |
|---|---|---|
| `sigma_8 = 0.811` (fail) | value correct, interpretation wrong | it is the LCDM value; `T(k)` changes sigma8 by 5e-5 |
| `S_8 = 0.829` (pass) | **retracted** | correct value is 0.8315, which is 1.7σ above target |
| S8 passes while sigma8 fails | **not attainable** | `S_8 = 1.025 * sigma_8` identically |
| Lyman-alpha ratio 0.891 (pass) | **retracted** | used `P = T·P` instead of `P = T²·P`, and averaged over points where `T ≡ 1` |
| Radion leakage produces `T(k)` | **falsified** | derived `G_eff` has the wrong sign, wrong shape, and a coupling excluded by ≥4 orders of magnitude |
| Screening fails by `10^42` | **withdrawn** | category error; the Lagrangian has no screening mechanism at all |

## The two central results

### 1. The transfer function cannot move sigma8

Only **0.048 %** of the sigma8 variance lies above `k = 1.5 h/Mpc`. A function
that is identically unity below that scale leaves sigma8 alone no matter what it
does above it. The measured change is `-4.8e-5` fractionally, five orders of
magnitude short of what would be needed.

This is a statement about filters, not about braneworlds, and it holds for any
modification of this form.

![window function](./v2.0/figures/fig1_window.png)

### 2. The published Lagrangian gives enhancement, not suppression

Reducing the published radion equation of motion in the quasi-static limit:

```
G_eff(k,a) / G  =  1 + 2 β² k² / (k² + a² m_eff²)
```

The correction goes as `β²`, so it is **positive at every scale and for every
choice of parameters**. A healthy scalar linearly coupled to matter mediates an
attractive force and increases clustering. It cannot lower sigma8. The shape is a
saturating step, not a declining power law. And because the coupling reaches
matter only through electromagnetic binding energy, the required strength is
excluded by Cassini and MICROSCOPE by at least four orders of magnitude.

None of this depends on the number of extra dimensions.

![G_eff](./v2.0/figures/fig4_geff.png)

## Repository layout

```
v2.0/
  radion_leakage_v2.0.pdf      the paper (16 pp, with appendices and errata)
  paper.tex                    LaTeX source
  V2.0_BASELINE_LOCKED.md      frozen Layer-1 control — do not edit
  verify_baseline.py           independent CAMB run + observable extraction
  make_figures.py              all five figures
  baseline_verification.json   numerical output
  pk_baseline.csv              P(k), T(k), and the sigma8 integrand
  figures/                     fig1..fig5 (300 dpi PNG)
```

Everything before `v2.0/` is retained for the record. Its observational
conclusions are superseded.

## Reproduce every number in the paper

```bash
git clone https://github.com/GeometricCosmo/gb-leakage-cmb.git
cd gb-leakage-cmb/v2.0
pip install camb numpy scipy matplotlib
python verify_baseline.py     # -> baseline_verification.json, pk_baseline.csv
python make_figures.py        # -> figures/
```

Under two minutes on one core. CAMB 2.0.4 was used; any version from 1.3 onward
should reproduce sigma8 to better than 1e-3.

## What is not affected

The 5D background numerics (warp factor solved to residual < 6e-6), the CAMB
pipeline infrastructure, and the reproducibility tooling are sound and unchanged.
The failure is in the observational analysis and in the attribution of the fitted
curve to the Lagrangian, not in the numerical machinery.

## What comes next

The single useful calculation is an **explicit dimensional reduction of the 5D
Gauss-Bonnet action**, carried far enough to determine whether the induced matter
coupling is conformal — as assumed in the v2.0 derivation — or of a derivative /
disformal type that could evade the sign argument. That is the one route by which
the mechanism could be revived.

Until that exists, neither a refit of the transfer function nor a move to 6D flux
compactification rests on anything. The proposed 6D programme is **deferred**:
the derived `G_eff` follows from a light scalar coupled linearly to matter through
`F²`, and that description survives dimensional reduction from any number of
dimensions.

Open blockers are listed in §7 and §8 of the paper.

## Version history

| Version | Claim | Status |
|---|---|---|
| v1.8.2 | exponential `T(k)` resolves small-scale abundances | superseded |
| v1.8.3 | `sigma_8 = 0.76` from the stated `T(k)` | incorrect, not reproducible |
| v1.9.0 | S8 / Lyman-alpha mutually exclusive; mechanism excluded | directionally correct |
| v1.9.1 | power-law `T(k)` passes S8 and Lyman-alpha | **retracted** |
| v2.0 | baseline fails; mechanism falsified | current |

The v1.9.0 conclusion was closer to correct than the v1.9.1 revision that
replaced it. The reversal traces to the two convention errors identified in §3 of
the v2.0 paper.

## Citation

```bibtex
@misc{Swart2026v2,
  title  = {A phenomenological power-law suppression of small-scale power:
            observational status, and why the published radion Lagrangian
            cannot produce it},
  author = {Swart, Andre},
  year   = {2026},
  note   = {Version 2.0},
  howpublished = {Zenodo}
}
```

## Contact

Andre Swart (GeometricCosmo) — geometriccosmo.illusion559@passinbox.com
Cape Town, South Africa

Corrections are welcome, particularly to the equivalence-principle estimate in
§5.3, which is schematic and should be replaced by a proper Damour-Donoghue
calculation with tabulated nuclear binding fractions.

---

*Publishing the refutation of your own result is the part of the method that
actually costs something.*
