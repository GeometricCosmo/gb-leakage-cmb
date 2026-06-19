# Data Setup for gb-leakage-cmb

**Complete guide to obtaining, organizing, and validating cosmological likelihood data for MCMC fits and observational constraints.**

---

## 📋 Quick Start

1. Create the data directory structure
2. Download likelihood packages from links below
3. Set environment variables
4. Run validation script
5. Test with example MCMC chain

**Estimated time:** 1–2 hours (mostly waiting for downloads)

---

## 📁 Directory Structure

After setup, your `data/` directory should look like:

```
data/
├── README.md                          (this file)
├── planck/
│   ├── plc_3.0/
│   │   ├── hi_l/
│   │   │   ├── plik_rd12_HM_v22_TT.clik
│   │   │   ├── plik_rd12_HM_v22_TE.clik
│   │   │   ├── plik_rd12_HM_v22_EE.clik
│   │   │   └── ...
│   │   ├── low_l/
│   │   │   ├── lowl_TT_clik_v1.p10.clik
│   │   │   └── ...
│   │   └── lensing/
│   │       ├── lensing_smicadx12_Dec5_ftl_mv2_ndclpp.clik
│   │       └── ...
│   └── 2018/
│       └── baseline/
│           ├── COM_PowerSpect_CMB-TT-full_R3.01.txt
│           ├── COM_PowerSpect_CMB-TE-full_R3.01.txt
│           └── ... (ASCII power spectra)
│
├── act_dr6/
│   ├── ACT_DR6_likelihood_v0.7.tar.gz  (or extracted)
│   ├── data_sacc_w_pointsources_allyears.fits
│   ├── act_planck_dr6_baseline_marged_tauprior_chi2.tar.gz
│   └── README.txt
│
├── spt3g/
│   ├── SPT3G_year1_cosmos_likelihood_v4.tar.gz  (or extracted)
│   ├── spt3g_year1_TT_clik.fits
│   ├── spt3g_year1_TE_clik.fits
│   └── README.txt
│
├── weak_lensing/
│   ├── des_year3/
│   │   ├── DES_Y3_3x2pt_data_vectors.fits
│   │   ├── DES_Y3_3x2pt_covariance.fits
│   │   └── DES_Y3_galaxy_sample_properties.txt
│   └── kids/
│       ├── KIDS_450_cosmic_shear_power_spectrum.fits
│       ├── KIDS_450_shear_covariance.fits
│       └── ...
│
├── lyman_alpha/
│   ├── desi_dr1/
│   │   ├── DESI_Lyman_alpha_flux_power.fits
│   │   ├── DESI_Lyman_alpha_covariance.fits
│   │   ├── DESI_DR1_README.txt
│   │   └── ...
│   └── sdss/
│       ├── SDSS_Lyman_alpha_1D_PS.fits
│       └── ...
│
├── bbn/
│   ├── Planck_2018_BBN_YHe.txt
│   ├── Planck_2018_BBN_covariance.txt
│   └── README.txt
│
├── metadata/
│   ├── download_log.txt                (timestamps & versions)
│   ├── checksums.txt                   (SHA256 for verification)
│   └── licenses.txt                    (copy of all data licenses)
│
└── scripts/
    ├── download_all.sh                 (automated download script)
    ├── verify_downloads.py             (checksums & integrity)
    └── test_likelihood.py              (load test)
```

---

## 🌐 Data Sources & Downloads

### **CMB: Planck 2018 (High-ℓ, Low-ℓ, Lensing)**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **Planck Legacy Code (PLC v3.0)** | ~500 MB | [ESA Planck Archive](https://pla.esac.esa.int/#cosmology) | `.clik` binary |
| **High-ℓ TT/TE/EE** | Included in PLC | Same | `.clik` |
| **Low-ℓ TT** | Included in PLC | Same | `.clik` |
| **Lensing (MV2)** | Included in PLC | Same | `.clik` |
| **ASCII Power Spectra** | ~10 MB | [IRSA](https://irsa.ipac.caltech.edu/data/Planck/release_2/ancillary-data/) | `.txt` |

**Quick download:**
```bash
# Option 1: Manual (recommended for first-time)
# Go to: https://pla.esac.esa.int/#cosmology
# Download: "Planck Legacy Code (PLC) - All-in-one package"
# Extract: tar xzf plc_3.0.tar.gz

# Option 2: Automated (if available)
cd data/planck
wget -O plc_3.0.tar.gz "https://pla.esac.esa.int/pla/#download"
tar xzf plc_3.0.tar.gz
```

**Verification:**
```bash
# Check file sizes
ls -lh data/planck/plc_3.0/hi_l/*.clik
# Should be ~50-100 MB per file

# Load test (see test_likelihood.py)
python -c "import clik; clik.clik('data/planck/plc_3.0/hi_l/plik_rd12_HM_v22_TT.clik')"
```

**Citation:**
```bibtex
@article{Planck2018_Likelihood,
  author = {Planck Collaboration},
  title = {Planck 2018 results. XI. Constraints on cosmology from the cosmic microwave background power spectrum and lensing},
  journal = {A\&A},
  volume = {641},
  pages = {A11},
  year = {2020},
  doi = {10.1051/0004-6361/201833910}
}
```

---

### **CMB: ACT DR6 (Advanced ACT 2021–2023)**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **Full ACT DR6 likelihood** | ~200 MB | [LAMBDA/GSFC](https://lambda.gsfc.nasa.gov/product/act/) | `.fits` + Python |
| **TT/TE/EE covariances** | Included | Same | `.fits` |
| **Baseline MCMC chains** | ~1 GB | Same | `.txt` chains |

**Quick download:**
```bash
cd data/act_dr6
# Option 1: Use LAMBDA web interface (recommended)
# https://lambda.gsfc.nasa.gov/product/act/
# Download: "ACT DR6 Public Release Likelihood"

# Option 2: Direct wget (if direct link available)
wget -O act_dr6_likelihood.tar.gz "https://lambda.gsfc.nasa.gov/..."
tar xzf act_dr6_likelihood.tar.gz
```

**Setup for ACT:**
```bash
# The ACT likelihood is Python-based, not .clik
# Install the likelihood package:
cd data/act_dr6
python setup.py install --user

# Or add to PYTHONPATH:
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Citation:**
```bibtex
@article{ACT_DR6_2023,
  author = {ACT Collaboration},
  title = {The Atacama Cosmology Telescope: DR6 Lensing Maps and Cosmological Parameters from 2008–2018 Data},
  journal = {arXiv},
  eprint = {2307.XXXXX},
  year = {2023}
}
```

---

### **CMB: SPT-3G (South Pole Telescope, 2018–2020)**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **SPT-3G Year 1 likelihood** | ~100 MB | [LAMBDA/GSFC](https://lambda.gsfc.nasa.gov/product/spt/) | `.clik` |
| **TT/TE/EE spectra** | Included | Same | `.clik` |
| **Covariance matrices** | Included | Same | `.fits` |

**Quick download:**
```bash
cd data/spt3g
# Download from LAMBDA
# https://lambda.gsfc.nasa.gov/product/spt/
# File: "SPT-3G 2018-2020 Likelihood"

wget -O spt3g_likelihood.tar.gz "https://lambda.gsfc.nasa.gov/..."
tar xzf spt3g_likelihood.tar.gz
```

**Citation:**
```bibtex
@article{SPT3G_2023,
  author = {SPT Collaboration},
  title = {Constraints on Cosmology from the Cosmic Microwave Background Power Spectrum of the 2500-Square-Degree SPT-3G Survey},
  journal = {Phys. Rev. D},
  volume = {108},
  pages = {083529},
  year = {2023}
}
```

---

### **Weak Lensing: DES Year 3**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **DES Y3 3x2pt data** | ~500 MB | [DES Data Hub](https://des.ncsa.illinois.edu/) | `.fits` + `.sacc` |
| **Covariance matrix** | ~1 GB | Same | `.fits` |
| **Likelihood code** | ~50 MB | Same | Python module |

**Quick download:**
```bash
cd data/weak_lensing/des_year3

# Download via DES Data Hub
# https://des.ncsa.illinois.edu/releases/
# Files: DES_Y3_3x2pt_fiducial_v1.fits, covariance, etc.

# Or use wget if direct link available:
wget "https://des.ncsa.illinois.edu/releases/y3a2/..."
```

**Setup:**
```bash
# Install DES likelihood code
pip install des-y3-lensing-likelihood

# Verify
python -c "import des_y3_lensing; print(des_y3_lensing.__version__)"
```

**Citation:**
```bibtex
@article{DES_Y3_LSS_2022,
  author = {DES Collaboration},
  title = {Dark Energy Survey Year 3 Results: Cosmology from Galaxy Clustering and Weak Lensing},
  journal = {Phys. Rev. D},
  volume = {105},
  pages = {043512},
  year = {2022}
}
```

---

### **Weak Lensing: KiDS-450**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **KiDS-450 cosmic shear** | ~50 MB | [KiDS Data Release](https://kids.strw.leidenuniv.nl/) | `.fits` |
| **Covariance matrix** | ~100 MB | Same | `.fits` |
| **Likelihood code** | ~20 MB | Same | Python/Fortran |

**Quick download:**
```bash
cd data/weak_lensing/kids

# KiDS public data:
# https://kids.strw.leidenuniv.nl/
# Download: "KiDS-450 Public Release"

wget "https://kids.strw.leidenuniv.nl/releases/KiDS_450_cosmic_shear.tar.gz"
tar xzf KiDS_450_cosmic_shear.tar.gz
```

**Citation:**
```bibtex
@article{KiDS450_2021,
  author = {KiDS Collaboration},
  title = {KiDS-450: Cosmological parameter constraints from weak-lensing tomography},
  journal = {A\&A},
  volume = {646},
  pages = {A140},
  year = {2021}
}
```

---

### **Lyman-α: DESI DR1**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **DESI Lyman-α flux power** | ~100 MB | [DESI Data Releases](https://www.desi.lbl.gov/public/) | `.fits` |
| **Covariance & mock catalogs** | ~500 MB | Same | `.fits` |
| **Likelihood code** | ~50 MB | Same | Python |

**Quick download:**
```bash
cd data/lyman_alpha/desi_dr1

# DESI DR1 public release (2023)
# https://data.desi.lbl.gov/public/release/
# Look for: "Lyman alpha forest"

wget "https://data.desi.lbl.gov/public/release/dr1/lya/..." 
```

**Setup:**
```bash
# DESI likelihood is Python-based
pip install desilike

# Verify
python -c "from desilike.cosmo import Likelihood; print('OK')"
```

**Citation:**
```bibtex
@article{DESI_LyA_2024,
  author = {DESI Collaboration},
  title = {DESI 2024 Results. Part 1: Validation and Joint Analysis of the DESI and Planck Data},
  journal = {arXiv},
  eprint = {2404.XXXXX},
  year = {2024}
}
```

---

### **Lyman-α: SDSS (Legacy)**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **SDSS DR12 Lyman-α** | ~50 MB | [SDSS Data Archive](https://svn.sdss.org/public/data/) | `.fits` / `.txt` |
| **Covariance matrix** | ~100 MB | Same | `.fits` |

**Quick download:**
```bash
cd data/lyman_alpha/sdss

# SDSS public archive
# https://svn.sdss.org/public/data/sdss/DR12/
# Look for: "Lyman alpha flux power spectrum"

wget "https://svn.sdss.org/public/data/sdss/DR12/lya/..."
```

**Citation:**
```bibtex
@article{SDSS_LyA_2017,
  author = {du Mas des Bourboux et al.},
  title = {Baryon Acoustic Oscillations from the SDSS-III Ly$\alpha$ Quasar Sample},
  journal = {A\&A},
  volume = {608},
  pages = {A130},
  year = {2017}
}
```

---

### **BBN: Primordial Abundances**

| Component | Size | Link | Format |
|-----------|------|------|--------|
| **Planck 2018 BBN constraints** | ~1 MB | [IRSA](https://irsa.ipac.caltech.edu/) | `.txt` |
| **Helium-4 & Deuterium** | Included | Same | `.txt` |
| **Covariance** | Included | Same | `.txt` |

**Quick download:**
```bash
cd data/bbn

# From Planck 2018 legacy products
# https://pla.esac.esa.int/#download
# Or direct:

wget "https://irsa.ipac.caltech.edu/data/Planck/release_2/auxiliary_data/ancillary_data/healpix_maps/README_bbn.txt"
```

**Citation:**
```bibtex
@article{Planck2018_BBN,
  author = {Planck Collaboration},
  title = {Planck 2018 results. VI. Cosmological parameters},
  journal = {A\&A},
  volume = {641},
  pages = {A6},
  year = {2020}
}
```

---

## ⚙️ Environment Setup

### **Set Environment Variables**

Add to your shell profile (`.bashrc`, `.zshrc`, or equivalent):

```bash
# Planck Legacy Code
export CLIK_PATH="${HOME}/path/to/gb-leakage-cmb/data/planck/plc_3.0"
export LD_LIBRARY_PATH="${CLIK_PATH}/lib:${LD_LIBRARY_PATH}"

# MontePython (if used)
export MONTEPYTHON_PATH="${HOME}/path/to/montepython_public"

# CosmoMC (if used)
export COSMOMC_PATH="${HOME}/path/to/cosmomc"

# Data directory
export GB_LEAKAGE_DATA="${HOME}/path/to/gb-leakage-cmb/data"
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

**Verify:**
```bash
echo $CLIK_PATH
echo $GB_LEAKAGE_DATA
```

### **Install Python Dependencies**

```bash
# Core dependencies
pip install numpy scipy matplotlib astropy
pip install emcee samplers

# Likelihood packages (choose as needed)
pip install cython  # required for CLIK
pip install actsdr6   # ACT likelihood
pip install des-y3-lensing-likelihood  # DES weak lensing
pip install desilike  # DESI Lyman-α

# Verification
pip freeze > data/metadata/requirements_installed.txt
```

### **Test Likelihood Loading**

```bash
# From repository root
python data/scripts/test_likelihood.py

# Expected output:
# ✓ Planck TT: OK
# ✓ Planck TE: OK
# ✓ Planck EE: OK
# ✓ ACT DR6: OK
# ✓ SPT-3G: OK
# ✓ DES Y3: OK
# ✓ DESI Lyman-α: OK
```

---

## ✅ Verification & Checksums

### **Download Verification Script**

```bash
cd data/scripts
python verify_downloads.py

# This checks:
# - File sizes
# - SHA256 checksums
# - Likelihood loading
# - Data range sanity checks
```

### **Manual Checksums**

If provided by data team, verify with:

```bash
# Generate SHA256 checksums
sha256sum data/planck/plc_3.0/*.tar.gz > /tmp/check.txt

# Compare with official checksums
diff /tmp/check.txt data/metadata/checksums.txt
```

### **File Size Quick Check**

```bash
# Expected file sizes (approximate)
du -sh data/planck/     # ~500 MB
du -sh data/act_dr6/    # ~200 MB
du -sh data/spt3g/      # ~100 MB
du -sh data/weak_lensing/  # ~2 GB
du -sh data/lyman_alpha/   # ~500 MB
du -sh data/bbn/        # ~1 MB
```

---

## 🔧 Troubleshooting

### **Problem: CLIK Not Found**

**Error:**
```
ImportError: libclik.so.7: cannot open shared object file
```

**Solution:**
```bash
# Ensure LD_LIBRARY_PATH is set
export LD_LIBRARY_PATH="${CLIK_PATH}/lib:${LD_LIBRARY_PATH}"

# Verify library exists
ls ${CLIK_PATH}/lib/libclik*

# If missing, rebuild CLIK:
cd ${CLIK_PATH}
./waf configure --install_all_deps
./waf install
```

### **Problem: Likelihood File Not Found**

**Error:**
```
FileNotFoundError: data/planck/plc_3.0/hi_l/plik_rd12_HM_v22_TT.clik
```

**Solution:**
```bash
# Check extraction
tar -tzf data/planck/plc_3.0.tar.gz | grep "plik_rd12" | head -5

# Re-extract if needed
rm -rf data/planck/plc_3.0/
tar xzf data/planck/plc_3.0.tar.gz -C data/planck/
```

### **Problem: Python Likelihood Import Fails**

**Error:**
```
ModuleNotFoundError: No module named 'actsdr6'
```

**Solution:**
```bash
# Reinstall specific package
pip install --upgrade --force-reinstall actsdr6

# Or build from source
cd data/act_dr6
python setup.py install --user

# Verify
python -c "import actsdr6; print(actsdr6.__file__)"
```

### **Problem: Likelihood Loads But Values Look Wrong**

**Error:**
```
Warning: χ² values are abnormally large (>10000)
```

**Solution:**
```bash
# Check if using correct data version
python data/scripts/test_likelihood.py --verbose

# Verify power spectrum normalization
python -c "import clik; l = clik.clik('data/planck/plc_3.0/hi_l/plik_rd12_HM_v22_TT.clik'); print(l.get_size())"

# Run on known-good model (ΛCDM best-fit)
python -m analysis.mcmc_driver --config examples/test_planck_ttee.ini
```

---

## 📊 Data Rights & Licensing

**All data sources are publicly available but have usage terms:**

| Source | License | Requirements |
|--------|---------|--------------|
| **Planck** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite official papers |
| **ACT** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite ACT collaboration papers |
| **SPT** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite SPT collaboration papers |
| **DES** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite DES collaboration papers |
| **KiDS** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite KiDS papers |
| **DESI** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite DESI papers |
| **SDSS** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Cite SDSS papers |
| **BBN** | Public domain | Cite Planck |

**Copy all licenses:**
```bash
# A copy of all terms is in:
cat data/metadata/licenses.txt
```

---

## 📝 Citation & Reproducibility

### **Always Cite Original Data Papers**

In your paper, include:

```bibtex
% CMB
@article{Planck2018_Likelihood,
  author = {Planck Collaboration},
  title = {Planck 2018 results. XI. Constraints on cosmology...},
  journal = {A\&A},
  volume = {641},
  pages = {A11},
  year = {2020}
}

% Weak lensing (choose one or more)
@article{DES_Y3_2022,
  author = {DES Collaboration},
  title = {Dark Energy Survey Year 3 Results...},
  journal = {Phys. Rev. D},
  volume = {105},
  pages = {043512},
  year = {2022}
}

% Lyman-α (choose one or more)
@article{DESI_LyA_2024,
  author = {DESI Collaboration},
  title = {DESI 2024 Results...},
  journal = {arXiv},
  eprint = {2404.XXXXX},
  year = {2024}
}
```

### **Document Data Versions**

Create a file `data/metadata/data_manifest.txt`:

```
# Data Manifest: gb-leakage-cmb
# Generated: 2026-06-18

Planck Likelihood Code v3.0
  Source: https://pla.esac.esa.int/#download
  Downloaded: 2026-06-18
  MD5: abc123...
  Version: plc_3.0

ACT DR6 Likelihood v0.7
  Source: https://lambda.gsfc.nasa.gov/product/act/
  Downloaded: 2026-06-18
  Version: dr6_public_v0.7

[etc.]
```

---

## 📈 Storage & Performance Tips

### **Storage Requirements**

```
Bare minimum (Planck only):        ~500 MB
Essential (Planck + ACT + SPT):   ~800 MB
Full suite (all):                  ~5 GB
With test chains/outputs:         ~50 GB
```

### **Disk Space Management**

```bash
# See where space is being used
du -sh data/*

# Archive large unused chains
tar czf data/archived_mcmc_chains_old.tar.gz data/chains_2024_01/
rm -rf data/chains_2024_01/

# Clean up temporary files
find data -name "*.tmp" -delete
find data -name "__pycache__" -type d -exec rm -rf {} +
```

### **Network Optimization**

```bash
# Use parallel downloads (if available)
# Example with GNU parallel:
cat urls.txt | parallel wget {}

# Resume interrupted downloads
wget --continue "https://..."

# Use data mirror if available
# Some data has multiple mirrors; choose closest to you
```

---

## 🧪 Testing & Validation

### **Run Quick Likelihood Test**

```bash
python data/scripts/test_likelihood.py --quick
# Takes ~1 minute
```

### **Run Full Validation**

```bash
python data/scripts/test_likelihood.py --full
# Takes ~10 minutes
# Tests all likelihoods on multiple models
```

### **Test MCMC Chain on Sample Data**

```bash
python -m analysis.mcmc_driver \
  --config examples/test_planck_only.ini \
  --n_steps 100 \
  --output data/test_run_output/
```

Expected runtime: ~5 minutes on modern CPU

---

## 🔄 Updating Data

### **When New Data Becomes Available**

```bash
# Download new version to separate directory
mkdir data/planck_new_2024
# Download new files here

# Run comparison test
python data/scripts/compare_likelihoods.py \
  --old data/planck/plc_3.0 \
  --new data/planck_new_2024

# If differences acceptable, update
mv data/planck/plc_3.0 data/planck/plc_3.0_backup_2024
mv data/planck_new_2024 data/planck/plc_3.0

# Document the update
echo "Updated Planck to plc_3.01 on 2024-XX-XX" >> data/metadata/update_log.txt
```

---

## 📚 Additional Resources

### **Tutorial Links**

- [Planck Legacy Code Tutorial](https://pla.esac.esa.int/#old_materials)
- [MontePython Documentation](https://github.com/brinckmann/montepython_public)
- [CosmoMC README](https://github.com/cmbant/CosmoMC)
- [DESI Likelihood Tutorial](https://desilike.readthedocs.io/)

### **Troubleshooting Guides**

- [CLIK Installation Issues](https://pla.esac.esa.int/pla/#old_materials)
- [MontePython FAQ](https://github.com/brinckmann/montepython_public/wiki)
- [ACT Data Release Notes](https://lambda.gsfc.nasa.gov/product/act/)

### **Contact for Data Issues**

- **Planck:** pla-support@esa.int
- **ACT:** [GitHub Issues](https://github.com/ACTCollaboration)
- **SPT:** spt-help@spt3g.org
- **DES:** help@des.lbl.gov
- **DESI:** [GitHub Issues](https://github.com/desihub)

---

## 📞 Questions?

**If you have issues:**

1. Check this README for FAQs and troubleshooting
2. Run `data/scripts/test_likelihood.py --verbose` to diagnose
3. Check the specific data team's documentation (links above)
4. Open a GitHub issue in this repository (tag `data-setup`)

**Questions about gb-leakage-cmb integration:**
📧 geometriccosmo.illusion559@passinbox.com

---

**Last updated:** June 2026  
**Maintainer:** Sparky (GeometricCosmo)  
**Version:** 1.7.3
