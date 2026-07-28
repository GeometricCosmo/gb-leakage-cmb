# Stage 3 Technical Report — Phase 1
## First-Principles Extraction of the Transfer Function from a 5D Einstein–Gauss–Bonnet–Radion System

**Status:** Phase 1 (equation-solving / relaxation approach) completed.
**Verdict (prompt Part 8.1 criteria):** **NO-GO for Phase 2 in the current formulation** — 2/4 criteria pass. Details in §6.

---

## 1. What was done

Per the Stage-3 prompt, we set up and solved the coupled background system on
the warped geometry

ds² = e^(−2A(y)) η_μν dx^μ dx^ν + dy²,

with a Gauss–Bonnet–corrected AdS vacuum, a quadratic radion potential
V(r) = −6 f∞ + ½ m² (r−r₀)² (cosmological constant fine-tuned RS-style), and a
brane-localized electromagnetic source S_EM(y) = −λ ρ₀ e^(−ρy) in the radion
equation. The 5D Einstein–scalar equations

A″ = −(1/3) r′²,
r″ = 4A′r′ + dV/dr + S_EM(y)

were solved as a boundary-value problem (scipy `solve_bvp`, tol 1e-8) with
junction conditions A(0)=0, A′(0)=k_eff, r(0)=r₀, r′(y_max)=0.

The Gauss–Bonnet coupling (λ_GB = 0.05, mid-range of the prompt's 0.01–0.1)
enters through the effective AdS curvature scale:
1 − f∞ + λ_GB f∞² = 0 ⇒ f∞ = 1.0557, k_eff = k_w √f∞ = 1.0275 k_w.

Radion mode functions φ_k(y) were then computed on this background from

φ_k″ − 4A′ φ_k′ − (k² e^(2A) + m²) φ_k = 0,

selecting the normalizable (decaying) branch, normalized at the brane
(φ_k(0)=1). The mode equation was integrated with a Riccati (log-derivative)
method, stable over the full k-range 10⁻⁴–10². **Validation:** against the
analytic pure-AdS solution (Bessel K_ν) the numeric transfer function agrees
to 0.1–3% across four decades in k.

## 2. Key result: the 5D transfer function is a broken power law, not a pure power law

The mode overlap β_r(k) = ∫ e^(−2A) φ_k dy has analytic asymptotics
(derivable in closed form for pure AdS, confirmed numerically on the
full background):

- **k ≪ k_eff:** β_r → const = 1/(ν k_eff), with ν = √(4 + m²/k_eff²)
- **k ≫ k_eff:** β_r ∝ k⁻¹ (exact asymptote, independent of ν)

The two regimes join in a transition centered at k ~ k_eff, roughly two
decades wide. The local logarithmic slope d ln β_r / d ln k runs smoothly
from 0 to −1. **A pure power law over the full phenomenological band
(0.1–20 h/Mpc) is mathematically impossible in this framework** — the slope
passes through −1/2 only within the transition region.

## 3. Comparison with the v1.8.3 target T(k) = (1.5/k)^0.5

Two extraction prescriptions were tested against the target (free overall
normalization, standard for transfer functions):

### Prescription A — T(k) = ∫ e^(−2A) φ_k dy (prompt Part 3.1 step 4)
Best case after scanning ν ∈ [0.3, 3.0] and k_eff ∈ [0.5, 50] h/Mpc:

- Best fit: ν = 0.30 (m² = −3.91 k_eff², i.e. **0.09 above the BF bound**),
  k_eff = 2.9 h/Mpc
- RMS log-deviation: 0.141 ⇒ **mean |Δ| = 12.1%, max |Δ| = 25.2%**
- The required radion mass is essentially at the Breitenlohner–Freedman
  stability bound — a pathological corner of parameter space, not a robust
  prediction.

### Prescription B — T(k) = √β_r(k) (prompt Part 6.1: "T(k) = √β_r(k)")
Notable positive finding: **the UV asymptote of √β_r is exactly k^(−1/2),
universally — independent of the radion mass ν and of λ_GB.** This is the
only sense in which the v1.8.3 exponent emerges "from geometry": it is the
high-k tail of the mode overlap, not a global property.

- With k_eff = 1.5 h/Mpc (the v1.8.3 pivot): RMS = 0.35–0.55 over the full
  band (poor), because the band straddles the flattening transition.
- Restricted to k ∈ [0.5, 20] h/Mpc with optimized k_eff ≈ 0.5 h/Mpc:
  mean |Δ| = 11.4%, max |Δ| = 28.4%.

### Summary table (prescription A, best-tuned case)

| k (h/Mpc) | T_v1.8.3 | T_Stage3 | Δ |
|---|---|---|---|
| 0.10 | 3.873 | 2.898 | −25.2% |
| 0.35 | 2.066 | 2.068 | +0.1% |
| 1.24 | 1.102 | 1.287 | +16.8% |
| 4.35 | 0.588 | 0.648 | +10.3% |
| 15.28 | 0.313 | 0.258 | −17.8% |

## 4. Go/No-Go scorecard (prompt Part 8.1)

| Criterion | Result | Pass? |
|---|---|---|
| Solver converges | BVP residual < 6×10⁻⁶; constraint O(0.2) due to EM source term (expected, source enters T_yy) | ✓ |
| T(k) matches v1.8.3 within 5% | Best achievable 12–15% (tuned), 25% max | ✗ |
| σ₈, S₈ within 3% of data | **Not testable here** — requires a CAMB/CLASS run with the recovered T(k); still pending | — |
| Runtime < 1 h | Full pipeline < 2 min | ✓ |

**Score: 2/4 → NO-GO** per the prompt's own criteria. The honest reading:
the mismatch is not an ansatz-convergence issue that Phase 2 (FEniCS/Dedalus
full PDE) would fix — the broken-power-law form is the *exact* analytic
behavior of the mode equation in a warped background. A finer solver will
reproduce the same curve more accurately.

## 5. Physical interpretation and red flags

1. **The exponent is prescription-dependent, not geometry-determined.**
   ∫e^(−2A)φ dy gives asymptote k⁻¹; √β_r gives k^(−1/2). The "derived"
   exponent depends on how the 5D solution is projected to 4D observables —
   precisely the step that v1.8.3 left implicit. Stage 3's real deliverable
   is therefore a *fixed projection prescription*, and it must be justified
   independently (holographic dictionary, 4D effective action normalization).

2. **The pivot 1.5 h/Mpc forces k_eff ~ 0.5–3 h/Mpc**, i.e. an extra-dimension
   curvature radius of hundreds of Mpc. As a fundamental RS warp factor this
   is in gross conflict with tests of gravity; it can only be interpreted as
   an effective IR scale of the radion sector, which needs explicit
   model-building to be consistent.

3. **Prescription A requires m² within 0.1 of the BF bound** — fine-tuned and
   potentially unstable once perturbation backreaction is included.

4. **The success criterion embeds the answer.** Matching a fitted
   phenomenological power law by tuning the potential V(r) (which the prompt
   leaves free) is a consistency exercise, not an ab-initio derivation. The
   geometry alone does not select (1.5/k)^0.5.

## 6. Recommendations

1. **Do not proceed to Phase 2 (full PDE) yet.** The bottleneck is the
   projection prescription and the k_eff scale, not solver accuracy.
2. **Fix the holographic dictionary first**: derive T(k) unambiguously from
   the 4D effective action (prompt Part 6.2, Z(k) route) and check whether
   the √β_r prescription is the physically correct one.
3. **Re-frame the success criterion**: instead of "match (1.5/k)^0.5 within
   5%", test the *actual* Stage-3 T(k) (broken power law) directly in CAMB
   against σ₈/S₈/Lyman-α data. It may fit the data better or worse than the
   v1.8.3 fit — that is the scientifically meaningful question.
4. **Address the k_eff scale problem** before any publication claim of a
   first-principles derivation.

## 7. Honesty statement (per prompt Part 12/13)

The Stage-3 Phase-1 solution does **not** confirm T(k) = (1.5/k)^0.5 as a
pure power law from geometry alone. It confirms: (i) the √β_r UV asymptote
has exponent −1/2 universally; (ii) a power-law-like behavior over a limited
k-window is achievable with tuning (12–15% accuracy); (iii) the claimed
confidence upgrade 70–75% → 85–95% is **not warranted** by these results.
Per the prompt's own decision tree ("If NO & disagrees": reassess), we
recommend the reframed test in §6.3 rather than a Phase-2 solver run.

## 8. Files

- `transfer_function_stage3_recovered.csv` — T(k), both prescriptions, 10⁻⁴–10² h/Mpc, 500 pts
- `warp_factor_stage3.csv` — A(y), A′(y) from the BVP solution
- `radion_profile_stage3.csv` — r(y), r′(y), effective mass
- `radion_potential_stage3.csv` — V(r), V′, V″
- `Tk_overview.png`, `Tk_comparison.png` — diagnostics and target comparison

*Computation: 5D Einstein–scalar BVP + Riccati mode solver, validated against
analytic AdS–Bessel solutions to 0.1–3%. λ_GB = 0.05, m² = −1.75 k_eff²
fiducial (scanned), EM source λρ₀ = 0.05 brane-localized.*
