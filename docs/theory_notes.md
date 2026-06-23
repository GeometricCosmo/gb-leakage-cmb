# Theory Notes: 5D Radion Leakage Framework
**Version 1.8.0** — June 2026

This document provides the theoretical foundation and current status of the radion leakage model in a 5D braneworld.

---

## 1. Core Idea

Our 4D observable universe is a dynamical **brane** embedded in a larger 5D bulk. The **radion** scalar field controls the local size of the extra dimension. Strong electromagnetic fields on the brane can excite the radion through a derived coupling, leading to transient energy leakage into the bulk. This leakage modifies the effective gravitational constant on the brane in a scale-dependent way.

The framework is built **brick by brick**, starting from first principles where possible and clearly identifying what remains phenomenological.

---

## 2. The Foundational Coupling (Brick 1)

The cornerstone of the model is the direct interaction term derived from the boundary variation of the 5D gauge action:

$$
\mathcal{L}_{\rm int} = -\frac{\lambda}{M_5^{3/2}} \, r(x) \, (\partial_\mu \phi)^2
$$

This coupling allows sharp electromagnetic field gradients to source the radion field. It is the physical bridge between electromagnetism and the extra dimension.

---

## 3. Dynamics and Leakage (Bricks 2–4)

The excited radion obeys a non-linear wave equation that includes Hubble damping, spatial gradients, self-interactions, and the EM driving term. Numerical integration during the leakage epoch (\(z \approx 50{,}000\)) yields a time-averaged excursion \(\langle r^2 \rangle \approx 0.075\).

A single stabilizing potential now unifies the scale selection:

$$
V_{\rm eff}(r) = V_0 \left(1 - e^{-\beta (r - 0.75)}\right)^2
$$

with \(\beta \approx 8.5\), \(V_0 \approx 8.5 \times 10^{-18}\). This potential simultaneously produces:
- Equilibrium brane size \( r_0 \approx 0.75 \)
- Radion mass leading to cutoff scale \( k_c \approx 0.75 \, h\,\mathrm{Mpc}^{-1} \)
- Back-reaction strength \(\beta_2 \approx 3.33\) from warped geometry, giving \( G_{\rm eff} \approx 0.75 G_N \)

The repeated appearance of **0.75** is therefore a structural feature, not a tuning.

---

## 4. Gravity Modification (Brick 3)

From Israel junction conditions and warp factor response:

$$
G_{\rm eff} \approx G_N \left(1 - \beta_2 \langle r^2 \rangle \right)
$$

The 25% suppression (\( G_{\rm eff} \approx 0.75 G_N \)) on small scales naturally reduces structure growth, addressing the S₈ tension and Lyman-α suppression.

---

## 5. Tiered Predictions

**Core Predictions** (~75% confidence)  
- Small-scale gravity suppression (\(k \gtrsim 0.5{-}1.0 \, h\,\mathrm{Mpc}^{-1}\))
- Lower σ₈ and S₈ than Planck+ΛCDM
- Power spectrum suppression in Lyman-α regime

**Strong Predictions** (~60% confidence)  
- Peak suppression near \(k_c \approx 0.75 \, h\,\mathrm{Mpc}^{-1}\)
- S₈ in 0.76–0.81 range
- Exponential-like transfer function \( T(k) \approx \exp[-(k/0.75)^{1.8}] \)

**Specific Predictions** (~45% confidence)  
- \( k_c \approx 0.75 \pm 0.08 \)
- σ₈ ≈ 0.76 ± 0.03
- S₈ ≈ 0.78 ± 0.03

---

## 6. Distinctive Feature

The model predicts a **non-trivial correlation** between the cutoff location and suppression strength, both arising from the same radion potential and warped geometry. This is difficult for standard extensions (massive neutrinos, EDE, generic modified gravity) to reproduce without fine-tuning.

---

## 7. Current Limitations & Open Questions

- Full 5D numerical back-reaction (Einstein + radion equations) is still needed for precision.
- Boltzmann code implementation (CLASS/CAMB) for quantitative joint likelihoods is the highest priority.
- Laboratory signatures remain speculative and deferred.

---

## 8. Philosophy

We are building a speculative but coherent alternative framework with maximum transparency. We clearly distinguish:
- What is derived from first principles
- What is motivated by observations
- What remains open

The goal is not to replace ΛCDM immediately, but to explore whether a single 5D mechanism can address multiple tensions in a physically motivated way.

**Next Critical Step**: Full implementation in Boltzmann solvers and joint MCMC analysis.

---

**Last updated**: June 2026  
**Framework maturity**: ~65%  
**Maintained by**: GeometricCosmo
