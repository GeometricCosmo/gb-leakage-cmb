# Radion Leakage in a 5D Braneworld: A Unified Framework for Cosmological Tensions

**Status:** Active Development | **Phase:** Theory + Numerical Validation  
**Latest:** v1.5.1 (June 2026) | **License:** MIT | **Contact:** geometriccosmo.illusion559@passinbox.com

---

## 🔗 Key Links

- **Full Theory Preprint:** https://zenodo.org/records/20607636
- **Educational Explainer:** https://the-leakage-theory.lovable.app/
- **GitHub Repository:** https://github.com/GeometricCosmo/gb-leakage-cmb

---

## Quick Summary

Our observable 4D universe may be a thin, dynamical membrane (**brane**) embedded in a larger 5D space. A scalar field called the **radion** controls the size of the extra dimension. When sharp electromagnetic fields excite the radion, energy leaks into the bulk, temporarily suppressing the effective gravitational constant and imprinting an exponential cutoff on the matter power spectrum.

**This single mechanism may explain multiple independent cosmological anomalies:**
- The **S₈ tension** (late-time structure less clumpy than early-universe predicts)
- **Lyman-α small-scale suppression** (less power in the intergalactic medium than ΛCDM)
- Hints of **modified expansion history** around z ≈ 50,000

**No new particles. One physics framework. Falsifiable predictions.**

---

## For Different Audiences

### 👨‍🔬 **Physicists & Cosmologists**
→ [Jump to *The Physics* section](#the-physics)

### 🤝 **Potential Collaborators**
→ [Jump to *Getting Involved* section](#getting-involved)

### ❓ **Skeptics & Curious Readers**
→ [Jump to *Why This Matters* section](#why-this-matters)

### 📚 **Students Learning Braneworld Physics**
→ [Jump to *Educational Roadmap* section](#educational-roadmap)

---

## The Physics

### Core Mechanism: Seven Bricks

This model is built from seven conceptual "bricks," each describing one piece of the physics. We show which are **derived from first principles**, which are **partially complete**, and which are **still under development**.

#### **Brick 1: Radion-EM Coupling** ✅ **DERIVED**

The electromagnetic field couples directly to the radion through boundary variation of the 5D gauge action:

$$\mathcal{L}_{\text{int}} = -\frac{\lambda}{M_5^{3/2}} \, r(x) \, (\partial_\mu \phi)^2$$

**Why this matters:** Sharp EM fields (high field gradients, asymmetric configurations) can excite the radion. This is derived, not assumed.

**Reference:** [Brick 1 full derivation](./docs/brick_1_radion_em_coupling.md)

---

#### **Brick 2: Radion Dynamics & Leakage** ◐ **PARTIAL**

The radion obeys a Klein-Gordon equation driven by EM stress:

$$\ddot{r} + 3H\dot{r} + V'(r) = -\frac{\lambda}{M_5^{3/2}} \langle (\partial_\mu\phi)^2 \rangle$$

**Current status:**
- ✅ RK45 numerical integration gives $\langle r^2 \rangle = 0.075 M_5^2$
- ⚠️ Full energy-conservation derivation for leakage fraction still in progress

**Reference:** [Brick 2 dynamics framework](./docs/brick_2_radion_dynamics.md)

---

#### **Brick 3: Gravity Modification** ◐ **FRAMEWORK**

The radion's displacement changes the extrinsic curvature via Israel junction conditions, leading to:

$$G_{\text{eff}} = G_N(1 - \beta_2 \langle r^2 \rangle)$$

**Current status:**
- ✅ Functional form derived from junction conditions
- ⚠️ Coefficient $\beta_2$ requires 5D Einstein equation solution
- **Goal:** Show that $\beta_2 \approx 3.3$ emerges naturally → $G_{\text{eff}} \approx 0.75 G_N$

**Reference:** [Brick 3 gravity coupling](./docs/brick_3_gravity_modification.md)

---

#### **Brick 4: Scale Selection** ⚠️ **OPEN**

Why does the characteristic scale appear as **0.75** in both:
1. Transfer function cutoff ($k_{\text{leak}} \approx 0.75$ h/Mpc)
2. Gravitational suppression ($G_{\text{eff}}/G_N \approx 0.75$)

**Current status:**
- ✅ Identified that $k_{\text{leak}}$ is likely the radion Compton wavelength
- ⚠️ Complete derivation of both scales from a single potential still needed

**Reference:** [Brick 4 scale selection](./docs/brick_4_scale_selection.md)

---

#### **Brick 5: Cosmological Impact** ◐ **OUTLINE**

How the modified $G_{\text{eff}}$ and transfer function affect:
- CMB damping tail
- S₈ and weak-lensing measurements
- Lyman-α forest
- Structure formation

**Current status:**
- ✅ Qualitative predictions correct (e.g., lower $\sigma_8$)
- ⚠️ Quantitative agreement requires full Boltzmann + N-body pipeline

**Reference:** [Brick 5 cosmology](./docs/brick_5_cosmological_impact.md)

---

#### **Brick 6: Stabilization & Relaxation** ◐ **PARTIAL**

How the radion returns to equilibrium after the leakage event.

**Current status:**
- ✅ Damped oscillator picture complete
- ⚠️ Full perturbative stability analysis pending

**Reference:** [Brick 6 stabilization](./docs/brick_6_stabilization.md)

---

#### **Brick 7: Laboratory Signatures** ◐ **SPECULATIVE**

Possible detection methods: asymmetric capacitor anomalies, precision EM tests, cosmological surveys.

**Current status:**
- ◐ Conceptually sound but highly tentative
- ⚠️ Requires careful null-hypothesis testing and collaboration with experimentalists

**Reference:** [Brick 7 lab signatures](./docs/brick_7_lab_signatures.md)

---

## Key Results (Current)

### Transfer Function Modification

$$T(k) = T_{\text{BBKS}}(k) \times \exp\left[ -\left( \frac{k}{0.75} \right)^{1.8} \right]$$

This produces:
- **Large scales** ($k < 0.1$ h/Mpc): Indistinguishable from ΛCDM ✓
- **Intermediate** ($0.1 < k < 0.75$ h/Mpc): Smooth transition
- **Small scales** ($k > 0.75$ h/Mpc): Exponential cutoff → reduced small-scale power

### Observable Predictions

| Observable | ΛCDM | This Model | Current Data | Status |
|-----------|------|-----------|--------------|--------|
| σ₈ | 0.811 | 0.76 | 0.76–0.79 | ✅ Agreement |
| S₈ | 0.832 | 0.78 | 0.790 | ✅ Tension reduced |
| Lyman-α (k > 1 h/Mpc) | Underpredicts suppression | Matches | DESI 2025 | ⚠️ Pending full fit |
| CMB damping tail (ℓ > 2000) | Standard | Slight suppression | ACT/SPT | ◐ Needs Boltzmann |
| Early-galaxy abundance | Too few | — | JWST | ❌ Mechanism retracted |

---

## Honest Assessment: What's Solid vs. What's Open

### ✅ **Derived from First Principles**
- Radion-EM coupling from 5D gauge action boundary variation
- Israel junction conditions with radion perturbation
- Dimensional analysis and scaling relations

### ◐ **Partially Derived / Well-Motivated**
- Radion dynamics via RK45 integration
- Functional form of $G_{\text{eff}}(r)$
- Transfer function cutoff shape

### ⚠️ **Still Open / Requires Computation**
- Explicit value of gravity-modification coefficient $\beta_2$ (from 5D Einstein equations)
- Origin of 0.75 scale (from potential structure)
- Joint fit to all cosmological data (Boltzmann + N-body)
- Full energy-conservation derivation of leakage fraction
- Laboratory signal magnitudes

### ❌ **Retracted Claims**
- **JWST early-galaxy boost:** Numerical analysis showed the mechanism has the wrong sign. Energy suppression on small scales produces fewer halos, not more. Claim removed; mechanism noted as open problem for future work.

---

## Repository Structure
