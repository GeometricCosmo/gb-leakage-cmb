# gb-leakage-cmb
# Radion Leakage in a 5D Braneworld Framework

**Work in Progress** — Active Development
For inquiries regarding collaboration, data chains, or seminar presentations, please open a GitHub Discussion or reach out via geometriccosmo.illusion559@passinbox.com.

This repository explores a 5D braneworld model in which our 4D observable universe is a dynamical membrane (brane) embedded in a larger 5D bulk. Strong electromagnetic fields on the brane can excite the **radion** — the scalar field controlling the local size of the extra dimension — leading to transient energy leakage into the bulk and a resulting modification of effective gravity on the brane.

The model was developed **brick by brick**, starting from first principles and guided by observations.

## Core Idea
https://zenodo.org/records/20607636

https://the-leakage-theory.lovable.app/

Our 4D universe (everything described by ΛCDM) represents only a thin dynamical layer in a much larger 5D space. The characteristic size of our brane in the extra dimension is approximately **0.75** (in normalized units). Deviations from this equilibrium size, driven by electromagnetic sources, produce observable effects in cosmology.

### Brick 1: Radion-EM Coupling (Strongest Foundation)
Derived from the boundary variation of the 5D gauge action in the ω → 0 limit:

$$
\mathcal{L}_{\rm int} = -\frac{\lambda}{M_5^{3/2}} \, r(x) \, (\partial_\mu \phi)^2
$$

This direct coupling allows strong, sharp electromagnetic fields to source the radion field.

### Dynamics
The radion obeys a non-linear wave equation that includes Hubble damping, spatial gradients, self-interactions, and the EM driving term (see diagram in repository).

### Phenomenological Consequences
Energy leakage into the bulk leads to a scale-dependent suppression of the effective gravitational constant \( G_{\rm eff}(k) \), most pronounced for \( k \gtrsim 0.75 \, h\,{\rm Mpc}^{-1} \).

This mechanism is being explored as a possible unified explanation for:
- Suppression in the CMB damping tail at high multipoles
- The S₈ tension
- Early structure formation hints (JWST)

## Current Status (Honest Assessment)

- **Brick 1** is derived from first principles and is solid.
- The non-linear radion dynamics and leakage current are physically motivated.
- The precise mapping from radion excursion to \( G_{\rm eff}(k) \) and the emergence of the 0.75 scale are still under active development (partly phenomenological at present).
- We are working toward a self-consistent model where a single mechanism addresses multiple cosmological tensions without introducing new particles.

## What the Model Does

A simple transfer function inspired by the underlying physics (for current testing):

$$
T(k) = \exp\left[ -\left( \frac{k}{0.75} \right)^{2.5} \right] \quad \text{for } k > 0.75 \, h\,{\rm Mpc}^{-1}
$$

Applied as \( P_{\rm mod}(k) = P_{\rm prim}(k) \times T(k)^2 \).

**Proven improvements** (from previous runs):
- Better fit to high-ℓ CMB damping tail (ACT DR6 + SPT-3G)
- Reduces S₈ toward weak lensing values
- Preserves large-scale successes of ΛCDM

**Current limitations**: Joint χ² still shows a penalty due to extra parameters. We are working to reduce this by deriving parameters from the 5D physics rather than fitting.

## Repository Contents

- `src/`: CAMB/CLASS patches implementing the leakage suppression
- `analysis/`: MCMC drivers and parameter scans
- `plots/`: Transfer functions, residuals, corner plots
- `docs/`: Theory notes, brick descriptions, and derivations
- `validation/`: Tests of the suppression mechanism

## Quickstart

(See original instructions — they remain valid)

## Development Roadmap (Current Priorities)

1. Finalize rigorous derivation of Brick 1
2. Derive gravity modification (Brick 2) from 5D geometry instead of fitting
3. Explain the origin of the 0.75 brane size scale from first principles (Brick 3/4)
4. Compute full cosmological impact on expansion history and structure formation
5. Explore laboratory signatures (high-voltage asymmetric capacitors in vacuum)

## Philosophy

This is not another small patch on ΛCDM. It is an attempt to view our universe as a dynamical 4D brane in a larger 5D space, where leakage between the brane and the bulk provides a physical mechanism behind several observed tensions.

**Data first. Transparency always. Hype later.**

— Andre Swart, June 2026

---
