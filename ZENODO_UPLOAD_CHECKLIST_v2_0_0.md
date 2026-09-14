"""
ZENODO UPLOAD CHECKLIST FOR v2.0.0
==================================

This is the EXACT step-by-step guide for what to select/fill in on Zenodo.
Follow this precisely to get the metadata right.
"""

print("""
═══════════════════════════════════════════════════════════════════════════════
ZENODO UPLOAD GUIDE - v2.0.0 (COMPLETE RECORD)
═══════════════════════════════════════════════════════════════════════════════

GO TO: https://zenodo.org/deposit

────────────────────────────────────────────────────────────────────────────────
STEP 1: START NEW RECORD
────────────────────────────────────────────────────────────────────────────────

Click "New upload" → Select "Publish my research"

────────────────────────────────────────────────────────────────────────────────
STEP 2: UPLOAD FILES
────────────────────────────────────────────────────────────────────────────────

Click "Choose files" or drag-and-drop. Upload in this order:

CATEGORY: DOCUMENTS
  ✓ ZENODO_v2_0_0_UPDATED_DESCRIPTION.md (this file, rename to abstract.md)
  ✓ BRICK_4_v1.9.0_REVISION.md (from your v1.9.0)
  ✓ transfer_function_optimization_results.md
  ✓ CDG2_test_report.md
  ✓ CHANGELOG_v1.9.0.md
  ✓ philosophy.md
  ✓ THEORY_ENGINE_SETUP_GUIDE.md
  ✓ QUICK_REFERENCE.md
  ✓ FINAL_VERDICT_TWO_CRITICAL_QUESTIONS.md
  ✓ COMPLETE_ANSWERS_TO_5_QUESTIONS.md

CATEGORY: CODE
  ✓ camb_pipeline_v1.9.0.py
  ✓ physics_engine_core.py
  ✓ camb_integration.py
  ✓ api_server.py
  ✓ test_suite.py
  ✓ question1_dynamic_kc_emergence.py
  ✓ question2_screening_equivalence_principle.py
  ✓ gradient_screening_critical_test.py

CATEGORY: DATA
  ✓ transfer_function_tests_results.csv

CATEGORY: FIGURES
  ✓ plot_1_transfer_function.png
  ✓ plot_2_cmb_spectrum.png
  ✓ plot_3_growth_rate.png
  ✓ plot_4_cdg2_abundance.png
  ✓ gb_model_v1.9.0_full_comparison.png
  ✓ dispersion_relation_4d.png
  ✓ transfer_function_evolution.png
  ✓ suppression_evolution_comparison.png

────────────────────────────────────────────────────────────────────────────────
STEP 3: BASIC INFORMATION
────────────────────────────────────────────────────────────────────────────────

TITLE: (Required)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Radion Leakage in 5D Gauss-Bonnet Braneworld: Power-Law Transfer Function, 
Observational Constraints, and Theoretical Viability Assessment
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTHORS: (Required)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Click "+ Add creators"
  Creator 1:
    Name: Swart, Andre
    Affiliation: GeometricCosmo (Independent Researcher)
    ORCID: [your ORCID if you have one]
    Role: Researcher
  
  Creator 2:
    Name: Claude (AI Assistant)
    Affiliation: Anthropic
    Role: Contributor (theory testing and falsification analysis)

DESCRIPTION/ABSTRACT: (Required — required minimum 20 characters)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Paste the full ABSTRACT from ZENODO_v2_0_0_UPDATED_DESCRIPTION.md]
[This is the 3000+ word description above]

────────────────────────────────────────────────────────────────────────────────
STEP 4: PUBLICATION INFORMATION
────────────────────────────────────────────────────────────────────────────────

PUBLICATION DATE: (Required)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Select: September 14, 2026 (or today's date)

TYPE OF PUBLICATION: (Required — Dropdown)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SELECT: "Preprint"
(Alternative: "Research Report" if you prefer)
DO NOT select "Published paper" (this isn't published yet)

────────────────────────────────────────────────────────────────────────────────
STEP 5: RESOURCE TYPE (Required — Critical!)
────────────────────────────────────────────────────────────────────────────────

This is in the "Additional Info" section (scroll down)

RESOURCE TYPE: (Dropdown)
SELECT: "Preprint" or "Research Report"

SUBTYPE (if available):
SELECT: "Pre-print"

OR if you want to be more specific:
SELECT: "Publication :: Preprint"

────────────────────────────────────────────────────────────────────────────────
STEP 6: KEYWORDS (Highly Recommended)
────────────────────────────────────────────────────────────────────────────────

Click "Add keyword" and add these (one per line):

✓ cosmology
✓ modified gravity
✓ scalar field
✓ braneworld
✓ 5D geometry
✓ radion
✓ electromagnetic coupling
✓ dark matter
✓ structure formation
✓ falsification
✓ equivalence principle
✓ theoretical constraints
✓ observational testing

────────────────────────────────────────────────────────────────────────────────
STEP 7: SUBJECTS (Recommended)
────────────────────────────────────────────────────────────────────────────────

Click in "Subjects" field and select:

PRIMARY SUBJECT:
  ✓ Physics - Cosmology and Extragalactic Astrophysics

SECONDARY SUBJECTS:
  ✓ Physics - General Relativity and Quantum Cosmology
  ✓ Physics - Astrophysics of Galaxies

────────────────────────────────────────────────────────────────────────────────
STEP 8: RELATED IDENTIFIERS (Recommended — Link to previous versions)
────────────────────────────────────────────────────────────────────────────────

Click "Add related identifier"

IDENTIFIER 1:
  Identifier: 10.5281/zenodo.20607636
  Relation type: "Is version of"
  Resource type: "Preprint"
  [This links to v1.9.0]

IDENTIFIER 2:
  Identifier: https://github.com/GeometricCosmo/gb-leakage-cmb
  Relation type: "Cites" or "Is supplemented by"
  Resource type: "Software"

────────────────────────────────────────────────────────────────────────────────
STEP 9: VERSION (Important!)
────────────────────────────────────────────────────────────────────────────────

In "Additional Info" → VERSION field:
TYPE: "2.0.0"

Zenodo will automatically assign a NEW DOI for this version.

────────────────────────────────────────────────────────────────────────────────
STEP 10: ACCESS & LICENSES
────────────────────────────────────────────────────────────────────────────────

ACCESS:
  SELECT: "Open Access"
  (Makes it publicly available immediately)

LICENSE:
  For code files (.py):
    SELECT: "MIT License"
  
  For documents (.md) and figures (.png):
    SELECT: "Creative Commons Attribution 4.0 International"
  
  For data (.csv):
    SELECT: "Creative Commons Zero (CC0) - Public Domain"

[Zenodo allows per-file licenses, so you can set different ones]

────────────────────────────────────────────────────────────────────────────────
STEP 11: OPTIONAL BUT RECOMMENDED
────────────────────────────────────────────────────────────────────────────────

CONTRIBUTORS:
Click "Add contributor"
  Name: [Your collaborators if any]
  Affiliation: [Their institution]
  Role: [Contributor, Supervisor, etc.]

FUNDING:
If you received any funding: Click "Add funding"
  Funder: [Name]
  Award: [Grant number]

ALTERNATE IDENTIFIER:
  arXiv: [if you post to arXiv]
  DOI: [if previously published elsewhere]

────────────────────────────────────────────────────────────────────────────────
STEP 12: REFERENCES (Optional but good practice)
────────────────────────────────────────────────────────────────────────────────

In the description, reference:
  • Li et al. (2025), ApJL 986, L18 — Candidate Dark Galaxy-2
  • Planck Collaboration 2018 — CMB constraints
  • DESI Collaboration 2024 — Large-scale structure
  • Gravity Probe B results
  • Eötvös balance experiment results

────────────────────────────────────────────────────────────────────────────────
STEP 13: PREVIEW & PUBLISH
────────────────────────────────────────────────────────────────────────────────

Click "Preview" to see how it looks.

Check:
  ✓ All files uploaded correctly
  ✓ Title is correct
  ✓ Authors listed
  ✓ Abstract is complete
  ✓ Keywords populated
  ✓ DOI field (Zenodo generates this automatically)

Click "PUBLISH" to finalize.

────────────────────────────────────────────────────────────────────────────────
AFTER PUBLICATION
────────────────────────────────────────────────────────────────────────────────

Zenodo will:
  ✓ Assign a new DOI (e.g., 10.5281/zenodo.XXXXXXX)
  ✓ Create a landing page
  ✓ Send confirmation email
  ✓ Make files publicly accessible

You will get:
  ✓ Permanent URL: https://zenodo.org/records/XXXXXXX
  ✓ Cite-as: DOI: 10.5281/zenodo.XXXXXXX
  ✓ BibTeX export
  ✓ Versioning through Zenodo's system

USE THIS IN YOUR PAPER:
  "We deposit all code, data, and analysis at:
   Swart, A. (2026). Radion Leakage in 5D Gauss-Bonnet Braneworld...
   Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX (v2.0.0)"

════════════════════════════════════════════════════════════════════════════════

CRITICAL METADATA SUMMARY (What Zenodo Cares About)
════════════════════════════════════════════════════════════════════════════════

REQUIRED:
  ✓ Title ✓ Authors ✓ Description ✓ Upload date ✓ Resource type

STRONGLY RECOMMENDED (for discoverability):
  ✓ Keywords ✓ Subjects ✓ License ✓ Related identifiers

OPTIONAL BUT HELPFUL:
  ✓ Version number ✓ Contributors ✓ Funding ✓ Alternate IDs

DO NOT FILL:
  ✗ DOI (Zenodo generates this)
  ✗ Publication dates (use upload date)
  ✗ Journal name (this isn't a journal paper yet)

════════════════════════════════════════════════════════════════════════════════

IF UPDATING AN EXISTING RECORD
════════════════════════════════════════════════════════════════════════════════

Instead of "New upload", you can:
  1. Go to your previous v1.9.0 record
  2. Click "New version"
  3. Update files, description, etc.
  4. Zenodo will automatically version it as v2.0.0

This links them together automatically (better for tracking evolution).

════════════════════════════════════════════════════════════════════════════════
""")
