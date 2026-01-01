# Theory Notes: Gauss–Bonnet Inspired Leakage Model

---

## 1. Motivation

Higher–curvature (Gauss–Bonnet) corrections in braneworld scenarios can modify graviton propagation at high comoving wavenumber \(k\).  
This motivates a smooth ultraviolet suppression of the primordial spectrum, potentially explaining residuals in high–ℓ CMB data.

---

## 2. Transfer Function

We adopt a phenomenological ansatz:



\[
T(k) = \exp\left[-2\left(\frac{k}{k_c}\right)^p\right]
\]



applied multiplicatively to the primordial spectrum:



\[
P_{\rm mod}(k) = P_{\rm prim}(k) \cdot T(k)^2
\]



- The exponent \(p\) is motivated to be near 2 but is allowed to vary in fits.  
- \(k_c\) sets the cutoff scale in comoving wavenumber.

---

## 3. Assumptions

- Perturbative regime: \(\alpha k^2 \ll 1\).  
- No light bulk scalars mixing strongly with gravity.  
- Brane tension tuned to recover 4D GR at low energies.  
- Linear CMB perturbations; standard nonlinear prescriptions for late–time structure.  
- Tensor modes remain localized (no anomalous B–modes expected).  

---

## 4. Limits

- Mapping from \((k_c, p)\) to fundamental 5D parameters is **model dependent**.  
- Reported bounds should be interpreted as **order–of–magnitude guidance only**.  

---

## 5. Observational Tests

- **Achromatic suppression**: frequency–independent across cleaned channels.  
- **Polarization signatures**: correlated suppression in TE and EE spectra; absence would falsify the model.  
- **No anomalous B–modes**: tensor sector unaffected.  
- **Cross‑dataset consistency**: suppression should appear in Planck, ACT DR6, and SPT‑3G spectra.  

---

## 6. Forecasts

- CMB–S4–like surveys can constrain \(k_c\) with  
  

\[
  \sigma(k_c) \approx 0.05 \ \mathrm{Mpc}^{-1}
  \]


- This provides a decisive test of the preferred parameter region.  
- Fisher forecasts and MCMC fits in `analysis/` scripts demonstrate expected sensitivity.  

---
