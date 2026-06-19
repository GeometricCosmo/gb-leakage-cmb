# Project Roadmap: Radion Leakage in 5D Braneworld

**Long-term vision:** Establish radion-EM coupling as a testable mechanism for S₈ and Lyman-α tensions through first-principles derivation, numerical validation, and peer-reviewed publication.

**Current status:** Theory + Numerical Validation (v1.7.2)  
**Next major milestone:** Peer-reviewed journal submission (target: Q4 2026)

---

## 🎯 Strategic Goals (Ranked by Priority)

| Goal | Timeline | Impact | Blocker |
|------|----------|--------|---------|
| **Derive β₂ from 5D Einstein equations** | Months 1–3 | Moves Brick 3 from ◐ to ✅ | Requires 5D gravity expertise |
| **Complete scale-selection mechanism** | Months 2–4 | Solves Brick 4 (critical gap) | Theoretical breakthrough needed |
| **Full Boltzmann + N-body pipeline** | Months 2–6 | Quantitative predictions for all observables | HPC resources, CLASS/CAMB expertise |
| **Joint likelihood fit (CMB + LSS + Lyman-α)** | Months 5–8 | Rigorous statistical validation | Requires Boltzmann pipeline first |
| **Peer-reviewed publication** | Months 8–12 | Establish credibility in literature | All above milestones must pass |

---

## 📋 Detailed Roadmap by Brick

### **Brick 1: Radion-EM Coupling** ✅ COMPLETE
**Status:** Fully derived and documented  
**What's done:**
- ✅ 5D gauge action boundary variation complete
- ✅ Explicit formula for λ derived: $\lambda = e^{-A(y_+)} / (\sqrt{6} \cdot g_5^2)$
- ✅ Full derivation document published (Zenodo)
- ✅ Ready for peer review

**What's left:**
- (Nothing — this brick is complete)

---

### **Brick 2: Radion Dynamics & Leakage** ◐ IN PROGRESS

#### **Phase 1: Numerical Validation** (Months 1–2) ✅ STARTING
**Milestones:**
- [ ] RK45 integration code refactored and documented
- [ ] Robustness analysis: vary initial conditions, coupling strength, potential form
- [ ] Generate 50+ runs with different parameters
- [ ] Quantify uncertainty on $\langle r^2 \rangle = 0.075 M_5^2$

**Success Criteria:**
- $\langle r^2 \rangle$ stable within ±20% across parameter variations
- All runs converge (no runaway solutions)
- Output matches published results to 5 significant figures

**Resources Needed:**
- 1 developer for 6-8 weeks
- Standard laptop (no HPC needed for this phase)

**Next Step → Phase 2**

#### **Phase 2: Energy-Conservation Derivation** (Months 3–4) ⏳ PLANNED
**Current state:** Leakage fraction formula assumed, not derived  
$$f_{\text{leak}} = \frac{\lambda^2 \langle r^2 \rangle}{M_5^3 + \lambda^2 \langle r^2 \rangle}$$

**What needs to happen:**
- [ ] Derive energy flux from bulk using Einstein equations
- [ ] Match to radion-field back-reaction term
- [ ] Show that the above formula emerges naturally
- [ ] Compare to RK45 results (validation)

**Success Criteria:**
- Formula derivation published in Brick 2 document
- Numerical results match derivation within 10%
- No ad-hoc parameters

**Resources Needed:**
- 1 theoretical physicist for 4-6 weeks
- Expertise in: junction conditions, energy conservation, 5D gravity

**Blocker:** None (can proceed in parallel with Brick 3)

---

### **Brick 3: Gravity Modification** ◐ IN PROGRESS

#### **Phase 1: Derive β₂ from 5D Einstein Equations** (Months 1–3) ⏳ PRIORITY
**Current state:** β₂ ≈ 3.3 is chosen to match observations, not derived  
$$G_{\text{eff}} = G_N(1 - \beta_2 \langle r^2 \rangle) \quad \Rightarrow \quad G_{\text{eff}} \approx 0.75 G_N$$

**What needs to happen:**
- [ ] Write down full 5D Einstein equations with radion perturbation
- [ ] Apply Israel junction conditions at brane boundary
- [ ] Extract gravitational response coefficient
- [ ] Show β₂ ≈ 3.3 emerges from first principles (or discover it's different)

**Success Criteria:**
- β₂ derived and published
- Matches observations if β₂ ≈ 3.3 (ideal case)
- If different value, understand why and retract/update claims

**Resources Needed:**
- 1–2 theoretical physicists for 8–12 weeks
- Expertise in: 5D Einstein equations, Israel conditions, perturbation theory
- Computational support: symbolic algebra (Mathematica/SymPy) for tensor calculations

**Blocker:** Requires 5D gravity expertise (is this available?)

**Alternative:** If full derivation not feasible in 3 months, document the gap explicitly in paper.

#### **Phase 2: Validate Against Brick 2 Results** (Months 4–6) ⏳ DEPENDS ON PHASE 1
- [ ] Compare gravity modification predictions to RK45 leakage dynamics
- [ ] Quantify self-consistency
- [ ] Publish Brick 3 complete derivation

**Success Criteria:**
- Gravity modification is self-consistent with leakage dynamics
- No unexplained parameters or ad-hoc choices

---

### **Brick 4: Scale Selection** ⚠️ CRITICAL RESEARCH PROBLEM

**Status:** Biggest unsolved piece of the framework

**Current understanding:**
- 0.75 appears in transfer function cutoff: $k_{\text{leak}} \approx 0.75$ h/Mpc
- 0.75 appears in gravity suppression: $G_{\text{eff}}/G_N \approx 0.75$
- These are **not the same thing** and need independent explanations
- Leading hypothesis: both trace to radion Compton wavelength $m_\phi = 2\pi/\lambda_{\text{Compton}}$

**What needs to happen:**
1. **Theoretical derivation:** From what potential structure does $m_\phi \sim 0.75$ h/Mpc emerge?
2. **Numerical validation:** Check if Goldberger-Wise potential naturally produces this scale
3. **Complete documentation:** Explain how both the 0.75 values follow from one mechanism

**Timeline:** Months 2–6 (long-term open problem)  
**Resources:** 1–2 theorists, 200+ GPU hours for parameter scans  
**Success Criteria:** Paper-ready derivation showing scale selection is natural, not tuned

**Importance:** **CRITICAL** — Without solving this, the model remains partially phenomenological

**Alternative approach:** If fundamental derivation impossible, document this explicitly and focus on testability instead.

---

### **Brick 5: Cosmological Impact** ◐ IN PROGRESS

#### **Phase 1: CLASS/CAMB Implementation** (Months 2–4) ⏳ PLANNED
**What's done:**
- Phenomenological transfer function at $k = 0.75$ h/Mpc
- MCMC analysis with Planck 2018

**What's needed:**
- [ ] Full Boltzmann code integration (CLASS or CAMB)
- [ ] Implement modified transfer function with smooth transition
- [ ] Compute CMB power spectra (TT, TE, EE, BB)
- [ ] Compute matter power spectrum
- [ ] Test against ACT DR6, SPT-3G, DESI

**Success Criteria:**
- CLASS/CAMB patches pass unit tests
- CMB predictions match baseline ΛCDM to <1% on large scales
- Small-scale suppression reproduces transfer function cutoff correctly
- Code is reproducible and documented

**Resources Needed:**
- 1–2 cosmologists / computational physicists for 10–14 weeks
- Expertise in: Boltzmann codes, numerical methods, cosmological likelihoods
- HPC: ~100 CPU-hours for test runs, ~1000 hours for full MCMC chains

**Collaboration opportunity:** Reach out to CLASS/CAMB developers for guidance

#### **Phase 2: N-body Simulations** (Months 4–8) ⏳ PLANNED
**What's needed:**
- [ ] Modify N-body code (Gadget, GAMER, or similar) to include modified gravity
- [ ] Run 20–50 simulations with different initial conditions
- [ ] Compute halo mass functions, matter power spectra, clustering
- [ ] Compare Lyman-α predictions to DESI 2025 measurements

**Success Criteria:**
- Halo mass function shows expected modifications
- Matter power matches transfer function predictions
- Lyman-α power at k > 1 h/Mpc matches DESI data within 2σ

**Resources Needed:**
- 1–2 N-body simulation experts for 12–16 weeks
- HPC: ~10,000 core-hours on supercomputer
- Expert access: XSEDE / NERSC / similar facilities

**Collaboration opportunity:** Seek N-body simulation expertise from community

#### **Phase 3: Joint Likelihood Fit** (Months 6–10) ⏳ PLANNED
**Once both Boltzmann and N-body are done:**
- [ ] Build joint likelihood combining CMB, weak-lensing, Lyman-α
- [ ] Run MCMC chains to constrain model parameters
- [ ] Compute figure-of-merit: how much does model improve fit to data?
- [ ] Compare to ΛCDM using Bayesian evidence

**Success Criteria:**
- Joint fit converges without degeneracies
- Model improves S₈ fit by > 2σ
- Lyman-α fit improves by > 1σ
- No new tension introduced elsewhere (BBN, Hubble, etc.)

**Resources Needed:**
- 1 statistician / cosmologist for 8–10 weeks
- HPC: ~5,000 core-hours for MCMC chains

---

### **Brick 6: Stabilization & Relaxation** ◐ IN PROGRESS

**Current state:** Damped oscillator picture is complete  
**What's missing:** Full perturbative stability analysis

**What needs to happen:**
- [ ] Analyze stability of radion around minimum of potential
- [ ] Check: does radion remain trapped, or does it run away?
- [ ] Compute decay timescale analytically
- [ ] Verify numerics match analytic predictions

**Timeline:** Months 3–5  
**Resources:** 1 theorist for 4–6 weeks  
**Success Criteria:** Publication-ready derivation of stabilization dynamics

**Importance:** Medium (necessary for consistency, but likely not blocking)

---

### **Brick 7: Laboratory Signatures** ◐ SPECULATIVE (DEFERRED)

**Current policy:** Not being actively pursued until Bricks 1–5 are validated.

**Why deferred:**
- Discussing applications before proving basic physics undermines credibility
- Similar to FOTR/MVMA: jumping to exotic claims too early is a red flag

**Future timeline:** If cosmological mechanism validates in 2027+, explore:
- [ ] Asymmetric capacitor configurations
- [ ] Precision gravity tests in lab
- [ ] Design experiments to detect local radion excitations

**Resources:** TBD (future collaboration with experimentalists)  
**Estimated timeline:** 18–24 months after cosmological validation

---

## 📊 Overall Timeline: Months 1–12

```
Month  1  |████████|  Brick 2 robustness + Brick 3 β₂ derivation START
Month  2  |████████|  Brick 2 analysis / Brick 3 in progress / Brick 4 research begins
Month  3  |████████|  Brick 2 phase 2 START / Brick 3 phase 2 START / Brick 5 CLASS/CAMB START
Month  4  |████████|  Brick 2 complete / Brick 5 N-body START
Month  5  |████████|  Brick 3 complete / Brick 4 ongoing / Brick 6 analysis
Month  6  |████████|  Brick 5 CLASS/CAMB complete / Joint likelihood START
Month  7  |████████|  Brick 5 N-body in progress / Likelihood chains running
Month  8  |████████|  Brick 5 N-body complete / Joint likelihood converging
Month  9  |████████|  Final joint likelihood results / Paper draft START
Month 10  |████████|  Paper writing & figures / Submit to journal (target: JCAP/PRD)
Month 11  |████████|  Referee review process
Month 12  |████████|  Revisions & publication
```

---

## ✅ Current Progress (v1.7.2)

| Brick | Status | Completion |
|-------|--------|-----------|
| **Brick 1** | ✅ Derived | 100% |
| **Brick 2** | ◐ Phase 1 in progress | 50% |
| **Brick 3** | ◐ Phase 1 starting | 20% |
| **Brick 4** | ⚠️ Research underway | 30% |
| **Brick 5** | ◐ Code phase starting | 15% |
| **Brick 6** | ◐ Partial | 60% |
| **Brick 7** | ⏳ Deferred | 0% |
| **Overall** | — | ~37% |

---

## 🚀 Critical Path to Publication

The shortest path to a peer-reviewed paper:

```
Brick 3 (β₂ derivation)
        ↓
Brick 2 (energy conservation)
        ↓
Brick 5 Phase 1 (Boltzmann pipeline)
        ↓
Brick 5 Phase 2 (N-body simulations)
        ↓
Brick 5 Phase 3 (joint likelihood fit)
        ↓
PAPER SUBMISSION (Month 10)
```

**Parallelizable work:**
- Brick 4 (scale selection) can proceed independently
- Brick 6 (stabilization) can be done anytime

**Blockers:**
- Brick 3 β₂ derivation must complete before full Boltzmann analysis
- Brick 5 N-body requires Brick 5 Boltzmann to be mature

---

## 🤝 Collaboration Opportunities

### **We're Actively Seeking:**

#### **5D Einstein Equation Experts** (Months 1–3)
- **What:** Derive β₂ from first principles
- **Time commitment:** 8–12 weeks
- **Impact:** Transforms Brick 3 from ◐ to ✅
- **Contact:** geometriccosmo.illusion559@passinbox.com

#### **Cosmological Simulation Experts** (Months 2–8)
- **What:** Implement modified gravity in CLASS/CAMB and run N-body
- **Time commitment:** 16–20 weeks (can be split across multiple people)
- **Impact:** Enables quantitative predictions and joint likelihood
- **Contact:** geometriccosmo.illusion559@passinbox.com

#### **Statistical Analysis / Likelihood Experts** (Months 6–10)
- **What:** Build and optimize joint likelihood fits
- **Time commitment:** 8–10 weeks
- **Impact:** Rigorous validation against all cosmological data
- **Contact:** geometriccosmo.illusion559@passinbox.com

#### **Theoretical Physics (Scale Selection)** (Months 2–6)
- **What:** Solve Brick 4 — why $m_\phi \sim 0.75$ h/Mpc?
- **Time commitment:** Open-ended research problem
- **Impact:** Biggest unsolved problem; closes the last theoretical gap
- **Contact:** geometriccosmo.illusion559@passinbox.com

### **How to Get Involved**

1. **Email with your expertise:** What do you specialize in?
2. **Discuss timeline:** How much time can you contribute?
3. **Define scope:** What specific work package interests you?
4. **Set up regular check-ins:** Weekly or bi-weekly meetings
5. **Plan for publication:** All major contributors become co-authors

---

## 📈 Success Metrics

### **Brick-by-Brick Validation:**

| Brick | Success Looks Like | Target Timeline |
|-------|-------------------|---|
| **Brick 1** | Already complete | ✅ Done |
| **Brick 2** | Leakage fraction derivation published | Month 4 |
| **Brick 3** | β₂ derived from first principles | Month 3–5 |
| **Brick 4** | Scale selection mechanism explained | Month 6 |
| **Brick 5** | Joint likelihood fit to all data | Month 8–10 |
| **Brick 6** | Stability analysis published | Month 5 |
| **Brick 7** | Deferred; framework designed | Month 12+ |

### **Publication Success:**

- ✅ Submission to JCAP or Physical Review D by Month 10
- ✅ Referee comments addressed within 2 rounds
- ✅ Publication by Q1 2027
- ✅ 10+ citations within 1 year of publication

### **Community Impact:**

- ✅ Repository used by 5+ research groups
- ✅ Follow-up papers building on this work
- ✅ Code actively maintained and extended
- ✅ Educational impact: students learn braneworld physics

---

## 🔄 Adaptive Planning

**This roadmap is a live document.** It will be updated:
- **Monthly:** As milestones are completed or revised
- **Quarterly:** As unexpected blockers or opportunities emerge
- **After major breakthroughs:** If new physics insights change priorities

**Versioning:** Each update will be timestamped and added to CHANGELOG.md

---

## 📝 How to Track Progress

**Real-time updates:**
- GitHub Issues: Tag with `roadmap` label
- Milestones: Organized by month and brick
- Project board: Kanban view of active work

**Monthly status reports:**
- Published in this README every first Monday of the month
- Includes: What was done, what's next, blockers, help needed

**Community visibility:**
- Open Slack/Discord channel (if interest warrants)
- Bi-weekly community calls (optional)

---

## 🎯 Long-Term Vision (Beyond Month 12)

**If the model validates:**
- Year 2 (2027): Extend to tensor perturbations, primordial gravitational waves
- Year 3 (2028): Laboratory experiments on local radion excitations
- Year 5+ (2030+): Full theory of braneworld-based dark matter and modified gravity

**If the model doesn't validate:**
- Publish honest assessment of what failed and why
- Document lessons learned for community
- Contribute to understanding of cosmological tensions
- Support alternative approaches

---

## 📞 Questions or Suggestions?

**Have ideas for the roadmap?**
- Open an Issue with label `roadmap-suggestion`
- Email: geometriccosmo.illusion559@passinbox.com
- Participate in community discussions

**Want to contribute?**
- Check [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines
- Review [COLLABORATION.md](./COLLABORATION.md) for active opportunities
- Email to discuss your expertise and interests

---

**Last updated:** June 2026  
**Next review:** July 2026  
**Maintained by:** Sparky (GeometricCosmo)
