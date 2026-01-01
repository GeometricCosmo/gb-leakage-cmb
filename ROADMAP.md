# Project Roadmap: gb-leakage-cmb

This roadmap outlines planned developments for the Gauss–Bonnet leakage model pipeline.

---

## ✅ Completed
- Core leakage patch (`src/camb_leakage_patch.py`)
- Validation scripts (`validation/`)
- Plotting utilities (`plots/`)
- ΔS8 scan + MCMC driver (`analysis/`)
- SLURM cluster scripts (`cluster/`)
- Documentation (`README.md`, directory READMEs, `docs/theory_notes.md`)
- Citation metadata (`CITATION.cff`)
- End‑to‑end reproducibility test (`tests/test_pipeline.py`)

---

## 🔜 Short‑Term Goals
- Add **polarization fits** (TE/EE suppression tests).
- Expand **examples/** with configs for ACT DR6 and SPT‑3G.
- Implement **Fisher forecast utility** (`analysis/fisher_forecast.py`).
- Improve plotting scripts with publication‑quality styles.

---

## 📈 Long‑Term Goals
- Integrate with **CMB‑S4 likelihoods** once available.
- Extend leakage ansatz to include **tensor sector tests**.
- Publish referee‑ready pipeline alongside arXiv paper.
- Encourage community forks for alternative modified gravity models.

---

## 🤝 Community Involvement
- Contributions welcome via pull requests (see `CONTRIBUTING.md`).
- Issues can be used to suggest new features or report bugs.
- Roadmap will be updated as milestones are reached.
