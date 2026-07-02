# Unified Description of Astrophysical Chemistry via Information Dynamics

**From D/H to Multi‑Element Isotopic Ratios**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20275479.svg)](https://doi.org/10.5281/zenodo.20275479)

---

## 📄 Overview

This repository contains the code and data accompanying the paper:

> **Unified Description of Astrophysical Chemistry via Information Dynamics: From D/H to Multi‑Element Isotopic Ratios**  
> *Published: July 1, 2026*  
> DOI: [10.5281/zenodo.20275479](https://doi.org/10.5281/zenodo.20275479)

For decades, astrochemistry has treated D/H, ¹⁵N/¹⁴N, and ¹²C/¹³C as independent probes of distinct physical processes, each with its own models and parameters. This work introduces the **locking coefficient** `f_lock` – a single parameter that simultaneously describes all three isotope ratios, revealing for the first time that they are governed by a common hidden variable.

---

## 🧠 Core Concept: The Locking Coefficient

The locking coefficient is defined as:

> **f_lock = ln( (D/H) / (D/H)_ISM )**

where `(D/H)_ISM = 1.5 × 10⁻⁵` is the interstellar medium reference value.

Once `f_lock` is determined from a body's D/H ratio, it predicts both its ¹⁵N/¹⁴N and ¹²C/¹³C ratios through a universal mapping.

---

## 🔬 Key Distinction: `p` vs. `f_lock`

| Concept | Symbol | Meaning |
|---------|--------|---------|
| **Information Purity** | `p` | The "genome" – natal order, determined by the birth environment |
| **Locking Coefficient** | `f_lock` | The "CV" – evolutionary retention, acquired over time |

This distinction provides a multidimensional perspective on isotopic fractionation.

---

## 📊 Validation

The model has been successfully validated against observational data from:

- ☀️ Sun  
- 🌍 Earth  
- 🌙 Moon  
- 🔴 Mars  

It also correctly identifies the evolutionary deviation of **comet 67P**, demonstrating robustness across diverse planetary bodies.

---

## 🔭 Key Prediction: 3I/ATLAS

The framework yields a quantitative, testable prediction for the interstellar object **3I/ATLAS**:

> **¹⁵N/¹⁴N = 1.70 × 10⁻³**

This counterintuitive result differs significantly from the Solar System value (2.3 × 10⁻³). The prediction is directly testable by **ALMA** or **JWST** within the next two years.

---

## 🚀 Applications

- Interstellar objects  
- Exoplanetary systems  
- Cross-scale connections between astrophysics and fundamental physics

---

## 📁 Repository Structure

```
.
├── data/               # Isotopic data for Solar System bodies
├── src/                # Analysis and visualization code
├── figures/            # Generated figures
└── paper/              # LaTeX source
```

---

## 📝 Citation

If you use this work, please cite:

```bibtex
@misc{huang2026unified,
  title={Unified Description of Astrophysical Chemistry via Information Dynamics: From D/H to Multi-Element Isotopic Ratios},
  author={Huang, Kai and Liu, Hongkui},
  year={2026},
  doi={10.5281/zenodo.20275479},
  url={https://doi.org/10.5281/zenodo.20275479}
}
```

---

*This work transforms isotopic fractionation from a collection of empirical correlations into a quantitative, predictive framework.*
