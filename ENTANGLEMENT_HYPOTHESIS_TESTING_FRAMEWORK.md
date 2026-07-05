# Radion Perturbation Framework: Mathematical Setup

**Phase 2 Technical Foundation for Entanglement Hypothesis Testing**

---

## Overview

This document establishes the explicit mathematical framework for computing holographic entanglement entropy in a radion-perturbed Randall-Sundrum geometry. It connects **existing derived results** (Bricks 1–3) with the **holographic entanglement computation** needed for Phase 3.

**No new physics here.** Only explicit equations using standard RS geometry + RT formula.

---

## Part 1: Background RS Metric (Unperturbed)

### Standard Randall-Sundrum Geometry

The 5D metric without radion perturbation:

$$ds^2 = e^{-2A(y)} \eta_{\mu\nu} dx^\mu dx^\nu + dy^2$$

where:
- $\eta_{\mu\nu}$ = 4D Minkowski metric (or FLRW if including cosmology)
- $y$ = extra dimension coordinate (orthogonal to branes)
- $A(y) = k|y|$ = warp factor (RS1 setup)
- $k$ = curvature scale (typically of order Planck mass or similar)

### Physical Interpretation

- Branes located at $y = 0$ (visible) and $y = L$ (hidden)
- Distance between branes = $L$ (related to radion)
- Exponential redshift factor $e^{-2A(L)}$ explains hierarchy

---

## Part 2: Radion as Extra Dimension Fluctuation

### Definition: Radion Field

The radion $r(x,t)$ describes the breathing mode — fluctuations in inter-brane distance:

$$r(x,t) = r_0 + \delta r(x,t)$$

where:
- $r_0$ ≈ 0.75 (equilibrium inter-brane separation, in normalized units)
- $\delta r(x,t)$ = small perturbation ($|\delta r| \ll r_0$)
- Depends on 4D spacetime $(x^\mu, t)$, not on bulk coordinate $y$

### Radion as Mode on Brane

The radion lives on the **4D brane**, but its fluctuations affect the **5D geometry**:

$$\text{Radion mode on brane} \quad \leftrightarrow \quad \text{Breathing of extra dimension}$$

When the radion oscillates:
- Inter-brane gap changes: $L \to L + \delta r(x,t)$
- Warp factor responds: $A(y) \to A(y) + \delta A(y, x, t)$

---

## Part 3: Perturbed Warp Factor

### Linear Response to Radion

When the radion displaces by $\delta r$, the warp factor shifts:

$$A(y) \to A(y) + \delta A(y, x, t)$$

**Linear approximation (valid for $|\delta r| \ll r_0$):**

$$\delta A(y, x, t) \approx \alpha(y) \cdot \delta r(x, t)$$

where $\alpha(y)$ is the **geometric response function** that comes from linearizing the 5D Einstein equations (Israel junction conditions).

### Key Points

1. **No new parameter:** $\alpha(y)$ is determined by RS geometry, not free to choose
2. **Linearization:** Valid because $\delta r \ll r_0$
3. **Factorization:** Separation of variables — $y$-dependence in $\alpha(y)$, $x$-dependence in $\delta r$

### Explicit Form (If Needed)

For RS1 with exponential warp:
$$\alpha(y) \sim e^{-A(y)} \quad \text{(order of magnitude)}$$

This can be derived from perturbed Einstein equations, but for now, treat it as a known function from 5D geometry.

---

## Part 4: Linearized Radion Wave Equation

### From Brick 2: The Radion's Equation of Motion

The radion satisfies a 4D scalar wave equation on the brane, including EM forcing:

$$\boxed{\ddot{\delta r} + 3H\dot{\delta r} - \frac{1}{a^2}\nabla^2 \delta r + m_r^2 \delta r + \text{(nonlinear)} = \frac{\lambda}{M_5^{3/2}} (\partial_\mu \phi)^2}$$

### Term-by-Term Explanation

| Term | Meaning | Source |
|:---|:---|:---|
| $\ddot{\delta r}$ | Acceleration in time | Standard kinematics |
| $3H\dot{\delta r}$ | Hubble friction | Cosmological expansion (FLRW metric) |
| $-\frac{1}{a^2}\nabla^2 \delta r$ | Laplacian (spatial diffusion) | 4D spatial Laplacian |
| $m_r^2 \delta r$ | Mass term | Radion effective mass (from potential V(r)) |
| RHS: $\frac{\lambda}{M_5^{3/2}} (\partial_\mu \phi)^2$ | EM forcing | Brick 1: radion-EM coupling |

### Key Facts (From Brick 2)

- **Radion mass:** $m_r \approx 1.27 \times 10^{-8}$ (ultralight scalar)
- **During leakage ($z \approx 50,000$):** EM energy is large, drives $\delta r$ oscillations
- **Amplitude:** RK45 integration gives $|\delta r| \approx 0.27 M_5$ (from Brick 2)
- **RMS displacement:** $\langle \delta r^2 \rangle \approx 0.075 M_5^2$ (observed; we want to derive this)

---

## Part 5: Holographic Entanglement Entropy Setup

### Ryu-Takayanagi Formula (Standard)

For a region $A$ on the boundary of AdS, the entanglement entropy is:

$$S_A = \frac{\text{Area}(\gamma_A)}{4G_N^{(d)}}$$

where $\gamma_A$ is the **minimal surface** in the bulk with boundary $\partial \gamma_A = \partial A$.

### For Braneworld Geometry

In RS geometry:
- Boundary = 4D brane at $y = 0$
- Bulk = 5D spacetime between branes
- Region $A$ = subset of boundary (e.g., small area on brane)
- Minimal surface $\gamma_A$ = surface in 5D minimizing area, with $\partial \gamma = \partial A$

**Metric for area calculation:**

$$ds^2_{\text{along surface}} = e^{-2A(y)} \delta_{ij} dx^i dx^j + dy^2$$

(The part of the full metric tangent to the surface)

### Area Element

Area of surface element:

$$dA_{\text{surface}} = \sqrt{-g_{\text{induced}}} \, d^3\xi$$

where $\xi$ parameterize the surface $(x^1, x^2, y)$.

---

## Part 6: Perturbation of Minimal Surface

### How Radion Fluctuations Affect Entanglement

When the radion perturbs, the geometry changes:
$$A(y) \to A(y) + \delta A(y, x, t) = A(y) + \alpha(y) \delta r(x,t)$$

This shifts the minimal surface:
$$\gamma_A \to \gamma_A + \delta \gamma_A$$

The area changes:
$$\text{Area}(\gamma) \to \text{Area}(\gamma) + \delta \text{Area}(\gamma)$$

### First-Order Variation

To first order in $\delta r$:

$$\delta \text{Area}(\gamma) = \int_\gamma \delta \sqrt{g_{\text{ind}}} \, d^3\xi$$

Using the perturbed metric:
$$\delta g_{\mu\nu}^{\text{ind}} \propto \delta A(y) = \alpha(y) \delta r(x,t)$$

**Result:**
$$\boxed{\delta \text{Area} \sim \int_\gamma \alpha(y) \delta r(x,t) \, dy}$$

(The exact coefficient depends on the integral, but the key point: area change is **proportional to** radion displacement)

---

## Part 7: Connection to Entanglement Entropy

### Entanglement Entropy Change During Leakage

From the area formula:

$$\delta S = \frac{1}{4G_5} \delta \text{Area} \propto \int_\gamma \alpha(y) \delta r(x,t) \, dy$$

**Time-average over leakage event:**

$$\langle \delta S \rangle = \beta_r \langle \delta r^2 \rangle$$

where $\beta_r$ is an effective "entanglement response coefficient" (depends on $G_5$, geometry, integral of $\alpha(y)$).

### Gravity Modification from Entanglement Suppression

From **Brick 3** (derived), we know:
$$G_{\text{eff}} = G_N (1 - \beta_2 \langle r^2 \rangle)$$

**Hypothesis:** The entanglement entropy suppression $\langle \delta S \rangle$ is directly related to gravity suppression:

$$\beta_2 \approx f(\beta_r, G_5, \text{geometry})$$

**Key Question (Phase 3):**
> Does the computed value $\beta_r$ (from holographic calculation) naturally give $\beta_2 \approx 3.33$?

If yes (without tuning) → Entanglement explains gravity suppression  
If no → Back to phenomenology

---

## Part 8: Summary of the Setup

### What We Have (Derived from Bricks 1–3)

| Quantity | Value | Source |
|:---|:---|:---|
| $r_0$ | ≈ 0.75 | Radion equilibrium (Brick 4 fitted) |
| $m_r$ | ≈ 1.27 × 10⁻⁸ | Radion mass from potential (Brick 2) |
| $\langle \delta r^2 \rangle$ | ≈ 0.075 M₅² | RK45 integration (Brick 2) |
| $\beta_2$ | ≈ 3.33 | Warped geometry derivation (Brick 3) |
| $G_{\text{eff}}$ | ≈ 0.75 G_N | Observed from S₈ measurements |
| $\alpha(y)$ | Geometry-determined | From RS metric (not free) |
| $k_c$ | ≈ 0.75 h/Mpc | Observed power cutoff |

### What We Need to Compute (Phase 3)

1. **Minimal surface $\gamma_A$** in perturbed RS geometry
2. **Area($\gamma$)** as function of $\delta r$ and geometry
3. **Entanglement response coefficient $\beta_r$** from holographic formula
4. **Predicted $\langle \delta r^2 \rangle$** from $\beta_r$ and gravity relation
5. **Compare to observed ≈ 0.075** — Does it match without tuning?

---

## Part 9: Computational Roadmap

### Phase 2 Tasks (Week 2)

**Task 1: Explicit RS Metric**
```
Write out:
  ds² = e^{-2k|y|} (-dt² + a²(t) d𝐱²) + dy²
  (including cosmological evolution a(t) if needed)
```

**Task 2: Identify Boundary Region A**
```
Choose: Small region on brane at position 𝐱₀
        OR momentum-space region (k > 0.75)
        (Physics determines which makes sense)
```

**Task 3: Write Minimal Surface Equation**
```
Extremize: ∫√(g_ind) d³ξ
Subject to: ∂γ = ∂A
Result: PDE for surface y(𝐱)
```

**Task 4: Perturbation Ansatz**
```
Assume minimal surface deforms: y(𝐱) → y₀(𝐱) + δy(𝐱)
where δy ∝ δr (proportional to radion)
```

### Phase 3 Task (Week 3): The Calculation

**Core Calculation:**
```
1. Solve PDE for y(𝐱) exactly or numerically
2. Compute Area = ∫√(g_ind) (in terms of δr)
3. Extract coefficient: Area ∝ f(δr)
4. Convert to entropy: S = Area / (4G₅)
5. Identify β_r from: ΔS ∝ β_r ⟨δr²⟩
6. CRITICAL TEST: Does β_r give β₂ ≈ 3.33?
```

---

## Part 10: Key Simplifications & Assumptions

### What We're Assuming (All From Literature)

- ✅ RS geometry is accurate (Randall-Sundrum, no modifications)
- ✅ Ryu-Takayanagi formula applies (standard holography)
- ✅ Linear perturbation theory valid ($|\delta r| \ll r_0$)
- ✅ Minimal surface exists (true for convex regions)
- ✅ Radion dynamics from Brick 2 (already computed)

### What We're NOT Assuming (To Avoid Phenomenology)

- ❌ No new parameters introduced
- ❌ No choice of form for $\delta A$ (comes from geometry)
- ❌ No free functions for $\alpha(y)$ (determined by RS)
- ❌ No adjustment of $\beta_r$ to match target

### If We Find Ourselves Assuming Anything Else

→ **RED FLAG: Stop and investigate.** That's where phenomenology hides.

---

## Part 11: Decision Points & Blockers

### Blocker 1: Minimal Surface Math

**Question:** Can we write down and solve the minimal surface PDE?

**If YES:** Continue to Task 4  
**If NO:** Math too hard. Either defer to expert or stop.

**Solution Strategy:** 
- Try analytical solution first (unlikely)
- Numerical solution (finite difference / finite element)
- Perturbative expansion in $\delta r$

### Blocker 2: Area Integral Convergence

**Question:** Does the area integral converge? Or does it diverge (need UV cutoff)?

**If FINITE:** Good, proceed normally  
**If DIVERGES:** Need to add regulator (introduces ambiguity)

**Standard approach:** Holographic entanglement usually has universal divergences; subtract them.

### Blocker 3: Coefficient Extraction

**Question:** Can we clearly identify $\beta_r$ from the calculation?

**If CLEAR:** Proceed to Phase 3 test  
**If AMBIGUOUS:** Investigate source of ambiguity

---

## Part 12: References & Formulas

### Key Papers to Cite

1. **Ryu & Takayanagi (2006)** — RT formula: $S = \text{Area}(\gamma) / (4 G_N)$
2. **Lewkowycz & Maldacena (2013)** — HRT formula (covariant version)
3. **Karch & Randall (2001)** — Entanglement in RS braneworld
4. **Randall & Sundrum (1999)** — Original RS geometry

### Standard Formulas (No Derivation Needed)

**Minimal surface equation (Euler-Lagrange):**
$$\nabla \cdot \left( \frac{\nabla f}{\sqrt{1 + |\nabla f|^2}} \right) = 0$$

**Area element (hypersurface):**
$$dA = \sqrt{\text{det}(g_{\text{ind}})} \, d^3\xi$$

**Entanglement entropy (RT):**
$$S = \frac{1}{4G_N} \text{Area}(\gamma_A)$$

---

## Part 13: Expected Outcomes & Next Steps

### If Calculation Succeeds (Phase 3)

```
Predicted ⟨δr²⟩ from holographic calculation
         ↓
Compare to observed ≈ 0.075 M₅²
         ↓
IF match (±20%): ✅ Natural derivation
                    Proceed to new predictions
                    
IF close (30–50%): ⚠️ Minor discrepancy
                    Investigate source
                    
IF mismatch (>50%): ❌ Doesn't work
                    STOP exploration
```

### Documentation

If Phase 3 succeeds:
- Write up detailed calculation (methods section)
- Show all steps (for reproducibility)
- Document any assumptions made
- List limitations

If Phase 3 fails:
- Document why it failed (for archive)
- Identify where phenomenology entered
- Note for future theorists

---

## Final Checklist (Before Starting Phase 2)

- [ ] RS metric explicitly written (with A(y) = k|y|)
- [ ] Radion field defined (r = r₀ + δr)
- [ ] Perturbed warp formula clear (δA ∝ α·δr)
- [ ] Wave equation (Brick 2 result) stated
- [ ] Minimal surface problem formulated
- [ ] Area variation from perturbation understood
- [ ] Connection to entanglement entropy clear
- [ ] Gravity suppression relation (Brick 3) referenced
- [ ] Blockers identified (math, convergence, coefficient extraction)

---

**This is your roadmap. Use it to navigate Phase 2 systematically.**

No invention. Only explicit computation from known RS geometry and RT formula.
