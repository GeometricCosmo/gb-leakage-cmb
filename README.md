# Radion Leakage in 5D Gauss-Bonnet Braneworlds

**Independent Verification: The Phenomenological Baseline and the Proposed Mechanism Are Both Falsified**

<div align="center">

![Status](https://img.shields.io/badge/Status-Negative_Result-red?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0.0-purple?style=for-the-badge&logo=github)
![Physics](https://img.shields.io/badge/Physics-5D_Braneworld-blue?style=for-the-badge)
![Integrity](https://img.shields.io/badge/Integrity-Retraction_Published-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**[📄 Paper (PDF)](./v2.0/radion_leakage_v2.0.pdf) • [🔒 Locked Baseline](./v2.0/V2.0_BASELINE_LOCKED.md) • [📦 Zenodo v1.9.1 (retracted)](https://zenodo.org/records/21663023) • [📧 Contact](mailto:geometriccosmo.illusion559@passinbox.com)</strong>**

</div>

---

## 🚨 CRITICAL UPDATE (September 2026)

**Status change:** the observational claims of v1.8.x and v1.9.x are **retracted**.
Independent CAMB verification at fixed $A_s$, followed by a direct derivation from
the published radion Lagrangian, shows that **neither the phenomenological curve
nor the proposed mechanism survives scrutiny.**

**What was claimed (v1.9.1):**
- ✅ $S_8 = 0.829$ — reported as a **pass**
- ⚠️ $\sigma_8 = 0.811$ — reported as a **constraint requiring modification**
- ✅ Lyman-α ratio $= 0.891$ — reported as a **pass**

**What independent verification found:**
- ❌ $\sigma_8$ moves by $-4.8\times10^{-5}$ — the mechanism does **nothing**
- ❌ $S_8$ and $\sigma_8$ are the **same measurement** ($S_8=1.025\,\sigma_8$); one
  cannot pass while the other fails
- ❌ The Lyman-α "pass" used a non-standard convention and two sampling points
  where the transfer function is a tautology; under the standard convention the
  suppression reaches **70% at $k=5\,h\,\mathrm{Mpc}^{-1}$** and is excluded
- ❌ The radion Lagrangian, correctly reduced, predicts **enhancement of
  clustering, not suppression** — the opposite of what is needed — at a coupling
  strength already excluded by four to thirteen orders of magnitude

This is a complete negative result at both the phenomenological and the
mechanistic level. It is published in full, with independent verification code,
because that is what the scientific record requires.

---

## 🔬 The Research Journey

### A Complete Record: From Hypothesis, Through a Wrong Turn, to Independent Verification

<div align="center">

```
STAGE 1               STAGE 2                    STAGE 3
──────────────────────────────────────────────────────────────────
Theoretical       ×   Observational          ×   Independent
Framework             Revision                   Verification

     ✅                  ❌ RETRACTED               ❌ FALSIFIED
  SOUND MATH           WRONG NUMBERS,           BOTH THE CURVE
  (unaffected)         WRONG CONVENTIONS        AND THE MECHANISM
```

</div>

---

## 📖 What This Repository Contains

<table>
<tr>
<td width="50%">

#### ✅ What Remains Sound
- **5D Einstein-Gauss-Bonnet geometry**, solved to residual $<6\times10^{-6}$
- **CAMB pipeline infrastructure**, fully reproducible
- **Independent verification code**, open and re-runnable in under two minutes
- **Complete documentation of the failure**, including a full derivation

</td>
<td width="50%">

#### ❌ What Is Retracted
- The claim that $T(k)=(1.5/k)^{0.5}$ passes $S_8$ and Lyman-α
- The claim that $\sigma_8$ is the only failing constraint
- The attribution of this transfer function to radion leakage
- The earlier "$10^{42}$ screening violation" (withdrawn as a category error,
  and replaced by a worse but correct statement: there is no screening at all)

**Result:** a fully negative result, published with the tools needed to check it.

</td>
</tr>
</table>

---

## 🎯 Quick Navigation

### For the Impatient
- **"Does it work?"** → No. See [The Two Failures](#-the-two-failures) below (3 min).
- **"Show me the numbers"** → [`baseline_verification.json`](./v2.0/baseline_verification.json)
- **"I want to check it myself"** → [`verify_baseline.py`](./v2.0/verify_baseline.py) (runs in under 2 minutes)
- **"Where's the derivation?"** → [Paper, §4–5](./v2.0/radion_leakage_v2.0.pdf)

### For the Thorough
- **Full paper with appendices and errata** → [`radion_leakage_v2.0.pdf`](./v2.0/radion_leakage_v2.0.pdf)
- **Frozen Layer-1 baseline (do not edit)** → [`V2.0_BASELINE_LOCKED.md`](./v2.0/V2.0_BASELINE_LOCKED.md)
- **Raw power spectra and the $\sigma_8$ integrand** → [`pk_baseline.csv`](./v2.0/pk_baseline.csv)
- **Figure generation script** → [`make_figures.py`](./v2.0/make_figures.py)

---

## 🔬 The Science: What Happened

### STAGE 1: Theoretical Development ✅ (unaffected)
**Timeline:** 2024–2025 | **Status:** Complete, still sound

We derived a model for EM-radion coupling in 5D geometry:

$$\ddot{r} + 3H\dot{r} - \frac{1}{a^2}\nabla^2 r + m_r^2 r + (\gamma + 3\beta)r^2 + \delta r^3 + \alpha r(\dot{r}^2 - (\nabla r)^2) = \frac{\lambda}{M_5^{3/2}}(\partial_\mu \phi)^2$$

- ✅ 5D geometry solved to residual $<6\times10^{-6}$
- ✅ Standard-sign kinetic term (not a ghost)
- ⚠️ The scale $k_c\approx1.5\,h\,\mathrm{Mpc}^{-1}$ was **fitted**, not derived, from
  the outset — this was always a phenomenological input, correctly labelled as
  such in earlier versions

### STAGE 2: Observational Revision ❌ (retracted)
**Timeline:** July 2026 | **Status:** Superseded

A power-law transfer function was fitted to 134 candidate shapes:

$$T(k) = \begin{cases} 1.0 & k < 1.5\ h\,\mathrm{Mpc}^{-1} \\ (1.5/k)^{0.5} & k \geq 1.5\ h\,\mathrm{Mpc}^{-1} \end{cases}$$

and reported to pass $S_8$ and Lyman-α while only $\sigma_8$ remained a problem.
**This report was incorrect** — see Stage 3.

### STAGE 3: Independent Verification ❌ (this version)
**Timeline:** September 2026 | **Status:** Complete

We froze the Stage 2 function and numbers as an immutable control, re-ran CAMB
2.0.4 at fixed $A_s$ (no amplitude rescaling), and separately derived the
effective gravitational coupling implied by the published Lagrangian.

**Corrected observational table:**

| Observable | v1.9.1 reported | Independently verified | Verdict |
|:---|:---:|:---:|:---|
| $\sigma_8$ | $0.811$, "fails" | $0.8112$ | this **is** the $\Lambda$CDM value — the mechanism changes it by $-4.8\times10^{-5}$ |
| $S_8$ | $0.829$, "passes" | $0.8315$ | $1.7\sigma$ high; **not** a pass |
| Lyman-α ratio | $0.891$, "passes" | $0.8125$ (standard convention) | wrong convention used; excluded once corrected |

Only **0.048%** of the $\sigma_8$ variance lies above the break scale $k_c$. A
function equal to 1 below $k_c$ cannot move $\sigma_8$, regardless of what it does
above it — this is a property of the top-hat filter, not of any specific theory.

---

## ❌ The Two Failures

### Failure 1 (Layer 1 — the curve itself)

$S_8$ and $\sigma_8$ are the same measurement up to a fixed factor,
$S_8 = 1.02501\,\sigma_8$, because $\Omega_m$ is fixed. **The reported pattern of
an $S_8$ pass alongside a $\sigma_8$ failure cannot occur for any transfer
function applied at $z=0$.** Both quantities sit $1.7\sigma$ above target. The
Lyman-α "pass" required applying $T$ to $P(k)$ instead of $T^2$, and averaging in
two sampling points at which $T\equiv1$ by construction. Under the correct
convention, suppression reaches 70% at $k=5\,h\,\mathrm{Mpc}^{-1}$ — excluded.

![Window function](./v2.0/figures/fig1_window.png)
![S8 vs sigma8](./v2.0/figures/fig2_s8_sigma8.png)
![Lyman-alpha](./v2.0/figures/fig3_lyman_alpha.png)

### Failure 2 (Layer 2 — the mechanism)

Reducing the published radion equation of motion in the quasi-static limit gives

$$\frac{G_{\rm eff}(k,a)}{G} = 1 + 2\beta^2\,\frac{k^2}{k^2+a^2 m_{\rm eff}^2}$$

This fails in three independent ways:

- **Sign:** the correction is $\propto\beta^2$, so it is positive for every real
  coupling. A healthy scalar linearly coupled to matter **enhances** clustering.
  It cannot lower $\sigma_8$.
- **Shape:** the response is a saturating Yukawa step (flat, then rising to a
  plateau), not a declining power law. No parameter choice converts one into
  the other.
- **Magnitude:** matching a percent-level shift needs $\beta\simeq0.2$. Because
  the coupling reaches matter only through electromagnetic binding energy, it is
  long-range and unscreened, and is excluded by Cassini ($\beta^2\lesssim10^{-5}$)
  and MICROSCOPE (schematically $\beta^2\lesssim10^{-14}$) — a shortfall of at
  least four, and plausibly many more, orders of magnitude.

The earlier report of a $10^{42}$ "screening violation" is **withdrawn as a
category error**: it measured the ratio of background source strengths, not a
screening factor. The Lagrangian contains no chameleon, symmetron or Vainshtein
mechanism at all — the corrected statement is worse than the one it replaces.

![G_eff derivation](./v2.0/figures/fig4_geff.png)
![Required vs permitted coupling](./v2.0/figures/fig5_coupling.png)

---

## 🧭 What Would Be Required, and What Is Deferred

A successor mechanism that still deserves the name "radion leakage" would need,
simultaneously:

1. **$\Delta G < 0$** — ruling out ordinary conformal scalar exchange entirely;
   requires either genuine energy transfer out of the matter sector or a
   derivative/disformal coupling.
2. **A suppression that does not drift in comoving $k$** — a fixed Compton
   scale $a\,m_{\rm eff}$ sweeps through all wavenumbers as $a\to0$; either
   $m_{\rm eff}\propto H$ or the model needs an explicit $T(k,z)$.
3. **A coupling that avoids the electromagnetic sector, or is genuinely
   screened** — the current route is closed by Section 5 of the paper.

**The proposed move to 6D flux compactification is deferred.** None of the three
failures above depends on the number of extra dimensions: $G_{\rm eff}$ follows
from any light scalar with a healthy kinetic term coupled linearly to matter
through $F^2$, in 5D, 6D, or otherwise. Flux compactification would determine how
$m_{\rm eff}$ and $\lambda$ are fixed; it would not change the sign of $\beta^2$.
Building a 6D foundation under a mechanism that already fails its own internal
consistency check is not the highest-leverage next step.

**The one calculation that could revive this line of work:** an explicit
dimensional reduction of the 5D action, carried far enough to check whether the
induced matter coupling is genuinely conformal (as assumed here) or of a
derivative/disformal type that could evade the sign argument. Until that exists,
neither a refit of $T(k)$ nor a move to 6D rests on anything.

---

## 💻 Code & Data

### Quick Start — reproduce every number in the paper
```bash
git clone https://github.com/GeometricCosmo/gb-leakage-cmb.git
cd gb-leakage-cmb/v2.0

pip install camb numpy scipy matplotlib

python verify_baseline.py     # -> baseline_verification.json, pk_baseline.csv
python make_figures.py        # -> figures/fig1..fig5.png
```
Runtime under two minutes on a single core. CAMB 2.0.4 was used; any version
from 1.3 onward should reproduce $\sigma_8$ to better than $10^{-3}$.

### Key Files
```
v2.0/
├── radion_leakage_v2.0.pdf        # the paper (16 pp, derivation + errata)
├── paper.tex                      # LaTeX source
├── V2.0_BASELINE_LOCKED.md        # frozen Layer-1 control — do not edit
├── verify_baseline.py             # independent CAMB run + observables
├── make_figures.py                # all five figures
├── baseline_verification.json     # numerical output
├── pk_baseline.csv                # P(k), T(k), sigma8 integrand
└── figures/
    ├── fig1_window.png            # why sigma8 can't move
    ├── fig2_s8_sigma8.png         # S8 and sigma8 are the same point
    ├── fig3_lyman_alpha.png       # the convention error
    ├── fig4_geff.png              # wrong sign, wrong shape
    └── fig5_coupling.png          # required vs. permitted coupling
```

Everything before `v2.0/` is retained for the historical record. Its
observational conclusions are superseded and should not be cited.

---

## 📊 Why We're Publishing a Negative Result

Most modified-gravity mechanisms fail $S_8$, or Lyman-α, or both, or require
extreme tuning. It was reasonable to check carefully whether this one was
different. It checked out the opposite way:

- ❌ The transfer function does not move the observable it was built to fix
- ❌ The claimed pass/fail split between two identical measurements is not
  mathematically possible
- ❌ The Lagrangian that was supposed to generate the curve predicts the
  opposite sign of effect

**Publishing this is the same scientific act as publishing the original
claim** — it just costs more, because it means retracting your own numbers in
public. The alternative, quietly revising the transfer function again without
flagging what changed, would be the actual failure here.

---

## 📞 Contact & Collaboration

**Lead Researcher:** Andre Swart (GeometricCosmo)
**Email:** geometriccosmo.illusion559@passinbox.com
**Location:** Cape Town, South Africa

### Open To
- **Checking** the equivalence-principle estimate in §5.3 of the paper, which is
  schematic and should be replaced with a proper Damour–Donoghue calculation
  using tabulated nuclear binding fractions
- **Collaborating** on the explicit 5D→4D dimensional reduction identified as
  the single highest-leverage next calculation
- **Community feedback** on whether a derivative/disformal coupling structure
  can be motivated from the existing 5D action

---

## 📖 How to Cite

```bibtex
@misc{Swart2026v2,
  title  = {A phenomenological power-law suppression of small-scale power:
            observational status, and why the published radion Lagrangian
            cannot produce it},
  author = {Swart, Andre},
  year   = {2026},
  note   = {Version 2.0 — supersedes the observational conclusions of
            versions 1.8.x and 1.9.x},
  howpublished = {Zenodo}
}
```

Please do **not** cite v1.9.1 for the $S_8$/Lyman-α resolution claim; it is
retracted (see Errata, Appendix D of the v2.0 paper).

---

## 📊 Project Status

<div align="center">

| Phase | Task | Status | Confidence |
|:---:|:---|:---:|:---:|
| **Stage 1** | 5D geometry theory | ✅ Complete, unaffected | 80% |
| **Stage 2** | Observational revision (v1.9.1) | ❌ Retracted | — |
| **Stage 3** | Independent verification (v2.0) | ✅ Complete | 99% |
| | | | |
| **Layer 1** | Phenomenological baseline | ❌ Falsified | 99% |
| **Layer 2** | Mechanism ($G_{\rm eff}$ derivation) | ❌ Falsified | 95% |
| **6D programme** | Flux compactification upgrade | ⏸ Deferred | — |
| **Next calculation** | Explicit 5D→4D reduction, coupling type | 🔜 Not started | — |

</div>

### Version History

| Version | Principal claim | Status after v2.0 |
|:---|:---|:---|
| v1.8.2 | Exponential $T(k)$ resolves dwarf-galaxy abundances | superseded |
| v1.8.3 | $\sigma_8=0.76$ from the stated $T(k)$ | incorrect, not reproducible |
| v1.9.0 | $S_8$/Lyman-α mutually exclusive; mechanism excluded | **directionally correct** |
| v1.9.1 | Power-law $T(k)$ passes $S_8$ and Lyman-α | **retracted** |
| **v2.0** | **Baseline fails; mechanism falsified** | **current** |

The v1.9.0 conclusion was closer to correct than the v1.9.1 revision that
replaced it. The reversal traces to two convention errors, both documented and
corrected in the v2.0 paper.

---

## 🎓 Scientific Integrity Statement

> This project froze its own claim, attacked it with an independent calculation
> at fixed amplitude, and reported what happened — including that the earlier
> "success" was an artifact of a convention error, and that the proposed
> mechanism predicts the opposite of the needed effect.
>
> We do not treat a $\sigma_8$ mismatch as an "opportunity" when it turns out
> $\sigma_8$ was never actually being tested. We do not describe a positive
> $\beta^2$ correction as a path forward when it enhances the exact quantity we
> are trying to suppress. A negative result reported in full is the outcome
> that keeps this record usable.

---

<div align="center">

## 🚨 The Bottom Line

**We built a 5D mechanism with sound background numerics.** ✅
**We fitted a curve to it and reported it passed two hard tests.** 📉
**Independent verification shows it changes nothing where it needs to, and
too much where it must not.** ❌
**The Lagrangian behind it enhances the wrong quantity, at a coupling already
excluded.** ❌
**We are publishing all of it, with the code to check every number.** ✅

This is what a **complete** negative result looks like.

---

**Latest Update:** September 2026 | **Version:** 2.0.0
**Status:** Independent Verification Complete — Layer 1 and Layer 2 Both Falsified
**Next:** Explicit 5D→4D dimensional reduction (coupling type undetermined)

</div>

---

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Powered by CAMB](https://img.shields.io/badge/Powered%20by-CAMB-purple.svg)](https://camb.info/)
![Status: Negative Result Published](https://img.shields.io/badge/Status-Negative%20Result%20Published-red)

</div>
