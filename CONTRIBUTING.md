# Contributing to gb-leakage-cmb

We welcome contributions to improve the Gauss–Bonnet leakage model pipeline and make it more useful for the cosmology community.

## 🛠 How to Contribute

1. **Fork the repo**  
   Create your own fork of [gb-leakage-cmb](https://github.com/GeometricCosmo/gb-leakage-cmb).

2. **Create a branch**  
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Make changes**  
   - Add new scripts, patches, or documentation.
   - Ensure code is reproducible and documented.
   - Follow the existing directory structure (`src/`, `analysis/`, `plots/`, etc.).

4. **Run tests**  
   Validate your changes with:
   ```bash
   python validation/test_suppression.py
   python tests/test_pipeline.py
   ```

5. **Commit and push**  
   ```bash
   git commit -m "Add feature: description"
   git push origin feature/my-new-feature
   ```

6. **Open a Pull Request**  
   Submit your PR to the `main` branch with a clear description of your changes.

---

## 📋 Guidelines

- **Coding style**: Pythonic, PEP8 compliant.  
- **Documentation**: Every new file should include a docstring explaining its purpose.  
- **Reproducibility**: Scripts must run end‑to‑end with provided configs.  
- **Testing**: Add unit tests in `validation/` or `tests/` for new features.  
- **Figures**: Save plots in `figures/` with descriptive filenames.  
- **Results**: Save numerical outputs in `results/` with `.npz` format.

---

## 🤝 Community Standards

- Be respectful and collaborative.  
- Cite relevant literature when adding new models.  
- Keep discussions constructive and focused on science.  

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.
```
