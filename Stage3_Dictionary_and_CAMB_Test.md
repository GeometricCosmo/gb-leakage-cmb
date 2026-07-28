# Stage 3 Technical Report — Phase 2
## Fixed Holographic Dictionary + Direct CAMB Test of the Recovered T(k)

**Status:** Both requested steps completed.
**Headline verdict: The model is falsified in its current form** (prompt Part 13, branch "NO & disagrees with data"). The claimed confidence upgrade to 85–95% is not merely unwarranted — the mechanism as specified **cannot produce its own claimed observables**.

---

## 1. The holographic dictionary, fixed from first principles

The arbitrariness flagged in the Phase-1 report is removed by deriving the
transfer function from the dimensionally reduced 4D effective action:

1. Expand the radion in orthonormal KK modes, r(x,y) = ∫ dμ r_μ(x) ψ_μ(y),
   with ∫ dy e^(−2A) ψ_μ ψ_μ′ = δ(μ−μ′), so the 4D fields r_μ are canonical.
2. A brane-localized EM source J(x)δ(y) (the prompt's own coupling) excites
   mode amplitudes r_μ = ψ_μ(0) J_k /(k² + μ²).
3. The brane observable is therefore governed by the **brane response function**

   **G(k) = ∫ dμ ρ(μ)/(k² + μ²),  ρ(μ) ≡ ψ_μ(0)²**

   — the unique, prescription-free object for "source on brane → response on
   brane". For pure AdS₅ with a Neumann brane the spectral density is exactly
   ρ(μ) ∝ μ^(2ν), ν = √(4 + m²/k_eff²). The radion 4D mass (from V″(r₀))
   gaps the spectrum at μ_gap; the warp scale cuts it off at μ_UV ~ k_eff.

4. **Transfer function: T(k) ≡ G(k)/G(0).** This is the only step where a
   choice was previously possible; it is now fixed.

### Consequences

- **Exponent fixed by geometry:** G(k) ∝ k^(2ν−1) in the regime
  μ_gap ≪ k ≪ k_eff. The v1.8.3 exponent −1/2 requires **ν = 1/4**, i.e.
  m_radion² = −63/16 k_eff² = −3.9375 k_eff². This is admissible (above the
  BF bound −4) and sits in the alternative-quantization window, but it is a
  *tuning*, not a prediction.
- **Low-k pathology repaired:** T(k) → 1 as k → 0 automatically (the raw
  (1.5/k)^0.5 blew up, violating CMB normalization). Calibration to the
  v1.8.3 pivot requires **μ_gap = 2.11 h/Mpc** (radion 4D mass
  ~ (1400 Mpc/h)⁻¹), and the full T(k) then matches the target to ~13% on
  k ∈ [0.8, 20] h/Mpc.
- **Scale separation restored:** unlike Phase-1 prescriptions (which forced
  k_eff ~ 1–3 h/Mpc), the continuum regime only needs k_eff ≫ 20 h/Mpc —
  the warp scale is no longer pinned to a cosmologically absurd value.

## 2. CAMB test (CAMB 2.0, Planck-2018 ΛCDM baseline)

Method: P_model(k) = P_ΛCDM(k) × T²(k) (standard transfer-function
modification, as used for WDM/ETHOS; background and growth unchanged).
Window-function σ8 integration validated against CAMB's `get_sigma8`
(0.8112 vs 0.8111 ✓).

### Results

| Case | σ8 | S8 | Δσ8 vs ΛCDM |
|---|---|---|---|
| ΛCDM (Planck 2018) | 0.811 | 0.832 | — |
| v1.8.3 T(k) = (1.5/k)^0.5 (clipped) | **0.811** | **0.831** | **−0.00%** |
| Stage-3 dictionary T(k) = G(k)/G(0) | **0.809** | **0.829** | **−0.30%** |
| v1.8.3 *claimed* | 0.760 | 0.779 | (−6.3%) |

Reference data: Planck σ8 = 0.811±0.006, S8 = 0.832±0.013;
KiDS-1000 S8 = 0.759±0.024; DES-Y3 S8 = 0.776±0.017.

### Finding A — the model cannot produce its own claimed σ8

The σ8 window function (R = 8 Mpc/h) has essentially zero weight for
k > 1.5 h/Mpc (W² < 3×10⁻⁴). Any transfer function that equals 1 below the
1.5 h/Mpc pivot and suppresses only above it **cannot move σ8 at all**.
v1.8.3's claimed σ8 = 0.760 from this T(k) is quantitatively impossible —
the number must have come from something other than running this transfer
function through a Boltzmann code.

### Finding B — the S8/Lyman-α no-go theorem

Scanning the only free scale (μ_gap):

| μ_gap (h/Mpc) | σ8 | S8 | P(5 h/Mpc)/P_ΛCDM |
|---|---|---|---|
| 0.10 | 0.607 | 0.622 | 0.011 |
| 0.20 | 0.709 | 0.726 | 0.023 |
| 0.40 | 0.771 | 0.790 | 0.050 |
| 0.80 | 0.798 | 0.818 | 0.107 |
| 2.11 (v1.8.3 pivot) | 0.809 | 0.829 | 0.300 |

- To touch the weak-lensing S8 ≈ 0.76 band the turnover must sit at
  μ_gap ≈ 0.3–0.4 h/Mpc — but then power at k = 5 h/Mpc is suppressed by
  **95–97%**, equivalent to sub-keV warm dark matter. Lyman-α forest data
  (m_WDM ≳ 3–5 keV, i.e. ≲15–20% suppression at those scales) rule this out
  by an enormous margin.
- Even at the v1.8.3 pivot (μ_gap = 2.11), the Lyman-α band gets ~70%
  suppression — already catastrophically excluded.

**There is no value of any parameter in this framework that satisfies both
S8 and Lyman-α.** With a k^(−1/2) amplitude law, the ~decade of lever arm
between the S8-sensitive band (k ~ 0.5–1.5 h/Mpc) and the Lyman-α band
(k ~ 2–8 h/Mpc) makes the two constraints mutually exclusive. This is a
structural property of the power-law mechanism, not a tuning problem.

## 3. Decision per the prompt's own tree (Part 13)

> **"If NO & disagrees with data: fundamental issue with mechanism; return to
> drawing board; publish falsification analysis instead."**

That is the branch we are on. Specifically:

1. The 5D solution is well-defined and the dictionary is now unique —
  that part of Stage 3 succeeded.
2. The geometry does yield k^(−1/2) — but only with ν = 1/4 tuned to within
  1.6% of the BF bound, and only as the mid-regime of a broken power law.
3. The resulting T(k), tested directly in CAMB, **fails**: it cannot
  generate the claimed σ8 reduction under any parameter choice without
  violating Lyman-α bounds by an order of magnitude.
4. Confidence assessment: the mechanism in its current form should be
  assigned **low confidence (<20%)**, not 85–95%. If anything is to be
  published, it is this falsification analysis.

### What would have to change to resurrect the idea
- A turnover in T(k) at k ~ 0.2 h/Mpc combined with a **much shallower**
  high-k tail (slope ≳ −0.2 in amplitude) to spare Lyman-α — i.e. abandon
  the k^(−1/2) law; or
- a mechanism acting on the growth rate / background (modified expansion,
  time-dependent leakage) rather than on the primordial-to-late transfer of
  power; or
- reinterpretation of the radion leakage as affecting only a sub-component
  of the matter density (partially-coupled DM), which can evade Lyman-α
  while still shifting S8 — that is a different model and would need its own
  Stage-1–3 program.

## 4. Files

- `transfer_function_stage3_dictionary.csv` — fixed-dictionary T(k), v1.8.3 comparison, power suppressions (500 pts)
- `camb_test_results_stage3.csv` — σ8/S8/Lyman-α outcomes for all cases
- `CAMB_test_stage3.png` — T(k) and P(k) comparison with S8/Lyman-α bands marked
- `Stage3_Phase1_Technical_Report.md`, `transfer_function_stage3_recovered.csv`, `warp_factor_stage3.csv`, `radion_profile_stage3.csv`, `radion_potential_stage3.csv` (Phase-1 outputs, still valid)

*Tools: CAMB 2.0 (Planck-2018 cosmology), spectral-representation solver for
G(k), window-function σ8 validated to 0.01% against CAMB internals.*
