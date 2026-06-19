# Security Policy

This document outlines the security practices and vulnerability reporting procedures for the **gb-leakage-cmb** repository.

---

## 📦 Supported Versions

Security patches and updates are provided for the following versions:

| Version | Release Date | Supported | Status |
|---------|--------------|-----------|--------|
| v1.7.2+ | June 2026+ | ✅ **Yes** | Current & Future |
| v1.7.0 – v1.7.1 | June 2026 | ✅ **Yes** | Backport available |
| v1.6.0 – v1.6.9 | June 2026 | ⚠️ **Limited** | Critical fixes only |
| v1.5.0 – v1.5.9 | June 2026 | ❌ **No** | Superseded |
| < v1.5.0 | Before June 2026 | ❌ **No** | Please upgrade |

**Recommendation:** Always use the latest stable version (`v1.7.2` or newer). Older versions may contain resolved security issues.

---

## 🛡️ Types of Security Issues We Track

We take the following categories of security issues seriously:

### 🔴 **Critical (Respond within 24 hours)**
- Remote code execution vulnerabilities
- Privilege escalation
- Data exfiltration or loss
- Cryptographic failures
- Injection attacks (SQL, code, etc.)
- Arbitrary file read/write via malicious input

**Example:** A bug allowing arbitrary Python code execution through a crafted CLASS configuration file.

### 🟠 **High (Respond within 48-72 hours)**
- Authentication bypass
- Cross-site scripting (XSS) in documentation or tools
- Denial of service attacks
- Unvalidated numerical output (producing wrong cosmological results)
- Dependency vulnerabilities with active exploits

**Example:** An external library used in numerical integration has a known vulnerability.

### 🟡 **Medium (Respond within 1-2 weeks)**
- Information disclosure (non-sensitive)
- Weak input validation (non-critical paths)
- Unpatched dependencies without known exploits
- Configuration issues

**Example:** User data directory world-readable due to incorrect permissions.

### 🟢 **Low (Include in regular release cycle)**
- Minor code quality issues
- Documentation clarifications
- Non-security warnings
- Best-practice improvements

---

## 🚨 Reporting a Vulnerability

If you discover a potential security vulnerability:

### **DO:**
✅ Report privately and directly to the maintainer  
✅ Include detailed reproduction steps  
✅ Allow reasonable time for investigation and patching  
✅ Use encrypted communication if the issue is especially sensitive  
✅ Follow responsible disclosure practices  

### **DO NOT:**
❌ Open a public GitHub issue  
❌ Post on social media or forums  
❌ Share details in pull requests or discussions  
❌ Attempt exploitation beyond what's necessary to confirm the bug  
❌ Demand immediate fixes or payments  

### **How to Report:**

**Option 1: Email (Recommended for sensitive issues)**
```
To: geometriccosmo.illusion559@passinbox.com
Subject: SECURITY: [Brief description]
```

Include:
- **Title:** Clear, non-descriptive summary (e.g., "Arbitrary Code Execution in Input Parser")
- **Description:** Detailed explanation of the vulnerability
- **Steps to Reproduce:** Exact commands or code to trigger the issue
- **Impact:** Who is affected and what damage could result
- **Affected Versions:** Which versions contain the bug (v1.7.2, v1.7.1, etc.)
- **Proof of Concept:** Minimal code or configuration that demonstrates the issue (if safe to share)
- **Suggested Fix:** Optional; your ideas on remediation (if you have them)

**Example Report:**

```
Subject: SECURITY: Unsafe NumPy Operations in Radion Dynamics

Description:
The RK45 integration in brick_2_radion_dynamics.py uses numpy.power() 
without input validation, allowing malformed exponents to crash the integrator.

Steps to Reproduce:
1. Run: python radion_dynamics.py --exponent "1/0"
2. Process dies with division by zero

Impact:
An attacker could trigger DoS via crafted input files in a 
shared computing environment.

Affected Versions:
v1.7.0, v1.7.1, v1.7.2

Suggested Fix:
Add bounds checking: if exponent < 0 or exponent > 10, raise ValueError
```

**Option 2: GitHub Security Advisory (for less sensitive issues)**
1. Go to your repository's **Security** tab
2. Click **Report a vulnerability**
3. Follow the guided form
4. We will respond within 48 hours

---

## 📋 Response Timeline

Once we receive your report:

| Timeline | Action |
|----------|--------|
| **Within 24 hours** | Acknowledge receipt of your report |
| **Within 48-72 hours** | Provide initial assessment (valid/invalid/disputed) |
| **Within 1 week** | Develop and test a fix (if confirmed) |
| **Within 2 weeks** | Release a patched version (if critical) |
| **Before public disclosure** | Notify you of the patch and publish details |

**For critical vulnerabilities:**
- We may release an interim patch to the latest version only
- Users of older versions are advised to upgrade immediately
- Public disclosure happens only after patches are released

---

## 📜 Responsible Disclosure & Coordination

### **Our Commitment:**
- ✅ We will investigate all reported vulnerabilities promptly and professionally
- ✅ We will keep you informed of progress
- ✅ We will credit you in release notes (unless you prefer anonymity)
- ✅ We will not prosecute good-faith security researchers
- ✅ We will coordinate disclosure timing to minimize harm

### **Your Commitment:**
- ✅ Give us reasonable time to patch (minimum 90 days before public disclosure)
- ✅ Do not publicly disclose details until we've released a fix
- ✅ Do not exploit the vulnerability beyond what's needed to confirm it
- ✅ Do not access or modify data that doesn't belong to you
- ✅ Act in good faith

### **Public Disclosure:**
Once a patch is released:
1. We will publish a security advisory in the GitHub **Releases** page
2. The advisory will include:
   - Description of the vulnerability
   - Affected versions
   - Patched versions
   - Impact assessment
   - Credit to the researcher (if desired)
3. You are welcome to publish your own technical analysis or blog post about the issue

---

## 🔐 Security Best Practices for Users

### **When Using This Code:**

#### **1. Always Use a Recent Version**
```bash
# Check your version
git describe --tags
# or
python -c "import gb_leakage_cmb; print(gb_leakage_cmb.__version__)"

# Update to latest
git pull origin main
```

#### **2. Validate Input Data**
- Don't trust cosmological configuration files from untrusted sources
- Verify file checksums when possible
- Sanitize paths and file names before passing to code

#### **3. Run in Isolated Environments**
```bash
# Use a Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### **4. Keep Dependencies Updated**
```bash
# Check for outdated packages
pip list --outdated

# Update everything safely
pip install --upgrade pip setuptools wheel
pip install --upgrade -r requirements.txt
```

#### **5. Use Version Pinning for Reproducibility**
```bash
# Generate a lockfile
pip freeze > requirements.lock

# Later, use the exact same versions
pip install -r requirements.lock
```

#### **6. Scan Dependencies for Vulnerabilities**
```bash
# Install safety
pip install safety

# Check for known vulnerabilities
safety check
```

---

## 🔧 Code Review & Quality Standards

### **What We Do:**
- ✅ Code review for all contributions (pull requests)
- ✅ Static analysis for common security issues
- ✅ Test coverage requirements (aim for >80%)
- ✅ Dependency scanning for known vulnerabilities
- ✅ Documentation of assumptions and limitations

### **What You Can Do:**
- Submit security-focused pull requests
- Suggest stricter input validation
- Propose security-related tests
- Report potential issues in code review

---

## 🚀 Patch Release & Deployment

### **When We Release a Security Patch:**

1. **Assign a version number** (e.g., v1.7.2-patch.1)
2. **Tag the repository** with the new version
3. **Publish a security advisory** in GitHub Releases
4. **Notify known users** (if contact information available)
5. **Update documentation** with security notes
6. **Archive the advisory** for future reference

### **For Users:**
- Patch releases are **backwards compatible** (no API changes)
- Simply pull the latest code or run `pip install --upgrade gb-leakage-cmb`
- Review the release notes to understand what was fixed
- No action needed beyond updating to the patched version

---

## 🔍 Vulnerability Research & Scope

### **In Scope for This Repository:**
- ✅ Bugs in Python code (our own files)
- ✅ Unsafe use of external libraries (our responsibility)
- ✅ Input validation issues
- ✅ Numeric correctness (if it breaks reproducibility)
- ✅ Documentation security (if it misleads users about safety)

### **Out of Scope:**
- ❌ Vulnerabilities in external libraries themselves (report to upstream)
- ❌ Hardware vulnerabilities (CPU spectre, etc.)
- ❌ Network infrastructure issues
- ❌ Server/deployment configuration (if you self-host)
- ❌ Issues in other people's code using our code

**Example Out-of-Scope Report:**
> "NumPy version 1.20.0 has a buffer overflow vulnerability"

**Response:** "Thank you. Please report this to NumPy directly. We recommend users update NumPy to version X.Y.Z or newer, which contains the fix."

---

## 📞 Security Contacts & Escalation

**Primary Contact:**
- 📧 Email: geometriccosmo.illusion559@passinbox.com
- ⏱️ Response time: Usually within 24-48 hours

**If No Response After 48 Hours:**
- Try reaching out again (emails sometimes bounce)
- Post a private GitHub Security Advisory
- Consider other communication channels if you have them

**Coordinated Disclosure Platform:**
- We accept reports via GitHub Security Advisories
- Link: https://github.com/GeometricCosmo/gb-leakage-cmb/security/advisories

---

## 🎯 Example Vulnerability Report (Good Format)

```
Title: Unvalidated Exponent in Power Spectrum Calculation

Description:
The transfer_function.py module uses numpy.power(k, exponent) without 
validating the exponent parameter. This allows a caller to provide 
NaN, infinity, or other invalid values that crash the integrator.

Steps to Reproduce:
1. Create a config file with exponent: "inf"
2. Run: python cosmology_interface.py --config malicious_config.yaml
3. Process terminates with floating-point error

Impact:
A shared computing environment could be disrupted by a user 
submitting jobs with malformed config files. Not exploitable for 
code execution, but causes denial of service.

Affected Versions:
v1.7.0, v1.7.1, v1.7.2 (latest)

Not Affected:
v1.6.9 and earlier (different calculation method)

Proof of Concept:
--- malicious_config.yaml ---
transfer_function:
  cutoff_exponent: inf
---

Suggested Fix:
In transfer_function.py, line 42:
Before: result = np.power(k, exponent)
After:  if not np.isfinite(exponent): raise ValueError(...)
        result = np.power(k, exponent)

Timeline:
I'm sharing this on June 18, 2026. If you need more time, please 
let me know your expected timeline. I plan to disclose publicly 
on September 18, 2026 (90 days) unless you've already patched.
```

---

## 📝 Changelog & Advisory Archive

We maintain a public record of all security advisories:

**Location:** [SECURITY_ADVISORIES.md](./docs/SECURITY_ADVISORIES.md)

Each advisory includes:
- Vulnerability description
- Affected versions
- Patch version
- Workarounds (if applicable)
- CVE number (if assigned)
- Credit to researcher

---

## ✅ Security Checklist for Contributors

If you're submitting code, please ensure:

- [ ] No hardcoded secrets, API keys, or passwords
- [ ] Input validation on all user-supplied parameters
- [ ] Error handling that doesn't expose sensitive information
- [ ] No SQL injection or code injection vulnerabilities
- [ ] Dependencies are up-to-date and vulnerability-free
- [ ] No unnecessary file write/read operations
- [ ] Permissions set correctly (e.g., `0o600` for sensitive files)
- [ ] No shell command injection (`os.system()` with user input is dangerous)
- [ ] Tests cover both happy path and error cases

---

## 🙏 Credits & Thanks

We appreciate the security research community. Researchers who report vulnerabilities responsibly will be credited in our releases and documentation (unless they prefer anonymity).

**Past Security Researchers:**
(To be updated as reports are received and resolved)

---

## 📚 References & Further Reading

**Responsible Disclosure:**
- [Responsible Disclosure Policy](https://responsibleDisclosure.com/)
- [CERT Coordination Center](https://www.cisa.gov/news-events/alerts)

**Security Best Practices:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [Scientific Code Best Practices](https://software.ac.uk/)

**Tools We Recommend:**
- [Safety](https://safety.readthedocs.io/) — Check for vulnerable dependencies
- [Bandit](https://bandit.readthedocs.io/) — Security issue scanner for Python
- [pip-audit](https://github.com/pypa/pip-audit) — Audit Python packages for known vulnerabilities

---

## 📞 Final Note

Security is a collaborative effort. Thank you for helping keep **gb-leakage-cmb** safe and secure for all users. If you have any questions about this policy, please reach out to the maintainer.

**Last Updated:** June 2026  
**Version:** 1.0  
**Status:** Active
