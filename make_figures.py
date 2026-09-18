#!/usr/bin/env python3
"""make_figures.py -- all figures for the v2.0 note."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
from scipy.integrate import simpson, solve_ivp
import os

OUT = "/home/claude/work/figures"; os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({
    "font.family": "serif", "font.serif": ["DejaVu Serif"], "font.size": 9,
    "axes.linewidth": 0.8, "axes.labelsize": 9.5, "axes.titlesize": 10,
    "xtick.direction": "in", "ytick.direction": "in",
    "xtick.top": True, "ytick.right": True, "legend.frameon": False,
    "legend.fontsize": 8.2, "figure.dpi": 200, "savefig.dpi": 300,
    "savefig.bbox": "tight", "mathtext.fontset": "dejavuserif",
})
C = dict(lcdm="#1a1a1a", mod="#c0392b", alt="#2471a3", warn="#e67e22",
         ok="#27ae60", grey="#8c8c8c")

d = np.loadtxt("/home/claude/work/pk_baseline.csv", delimiter=",", skiprows=1)
kh, pk, pkA, pkB, Tk, dsig2 = d.T
KC, R8 = 1.5, 8.0
OM, H0 = 0.31519, 67.36
ROOT = np.sqrt(OM/0.3)

# ============================================================== FIG 1
fig, ax = plt.subplots(2, 1, figsize=(5.6, 5.2), sharex=True,
                       gridspec_kw=dict(hspace=0.09, height_ratios=[1, 1.25]))
a = ax[0]
a.loglog(kh, Tk, color=C["mod"], lw=1.8, label=r"$T(k)$ (frozen baseline)")
a.loglog(kh, Tk**2, color=C["mod"], lw=1.2, ls="--",
         label=r"$T^2(k)$  (power suppression, $P\propto T^2$)")
a.axvline(KC, color=C["grey"], lw=0.8, ls=":")
a.text(KC*1.09, 0.062, r"$k_c=1.5\,h\,$Mpc$^{-1}$", fontsize=8, color=C["grey"])
a.set_xlim(1e-3, 30); a.set_ylim(0.04, 1.6)
a.set_ylabel("suppression factor"); a.legend(loc="lower left")
a.set_title("The frozen transfer function has no support where "
            r"$\sigma_8$ lives", fontsize=9.5)

b = ax[1]
b.semilogx(kh, dsig2, color=C["lcdm"], lw=1.6,
           label=r"$\mathrm{d}\sigma_8^2/\mathrm{d}\ln k$  ($\Lambda$CDM)")
m = kh >= KC
b.fill_between(kh[m], 0, dsig2[m], color=C["mod"], alpha=0.85, lw=0)
b.fill_between(kh[~m], 0, dsig2[~m], color=C["alt"], alpha=0.16, lw=0)
b.axvline(KC, color=C["grey"], lw=0.8, ls=":")
b.annotate("only 0.048 % of the\n"r"$\sigma_8$ variance lies here",
           xy=(2.6, 0.006), xytext=(5.0, 0.16), fontsize=8.2, color=C["mod"],
           ha="center", arrowprops=dict(arrowstyle="->", color=C["mod"], lw=0.9))
b.text(0.055, 0.28, "99.95 % of the variance\n"
       r"lies below $k_c$, where $T\equiv1$",
       fontsize=8.2, color=C["alt"], ha="center")
b.set_xlim(1e-3, 30); b.set_ylim(0, 0.42)
b.set_xlabel(r"$k\ \ [h\,\mathrm{Mpc}^{-1}]$")
b.set_ylabel(r"$\mathrm{d}\sigma_8^2/\mathrm{d}\ln k$"); b.legend(loc="upper right")
fig.savefig(f"{OUT}/fig1_window.png"); plt.close(fig)

# ============================================================== FIG 2
fig, a = plt.subplots(figsize=(5.4, 4.2))
s8 = np.linspace(0.70, 0.88, 50)
a.plot(s8, s8*ROOT, color=C["lcdm"], lw=1.4,
       label=r"$S_8=\sigma_8(\Omega_m/0.3)^{1/2}$, $\Omega_m=0.3152$ (fixed)")
a.axvspan(0.76-0.03, 0.76+0.03, color=C["ok"], alpha=0.13, lw=0)
a.axhspan(0.78-0.03, 0.78+0.03, color=C["ok"], alpha=0.13, lw=0)
a.axvline(0.76, color=C["ok"], lw=0.9, ls="--")
a.axhline(0.78, color=C["ok"], lw=0.9, ls="--")
a.plot(0.8112, 0.8315, "o", ms=9, color=C["mod"], zorder=5,
       label=r"baseline $T(k)$: $(\sigma_8,S_8)=(0.811,\,0.832)$")
a.plot(0.8111, 0.8315, "x", ms=9, mew=1.8, color=C["alt"], zorder=6,
       label=r"$\Lambda$CDM Planck 2018 — identical to 4 decimals")
a.annotate("claimed\n"r'"$\sigma_8$ FAIL"', xy=(0.8112, 0.756), fontsize=8,
           color=C["mod"], ha="center")
a.annotate("claimed\n"r'"$S_8$ PASS"', xy=(0.723, 0.8315), fontsize=8,
           color=C["mod"], ha="center", va="center")
a.plot([0.8112, 0.8112], [0.735, 0.8315], color=C["mod"], lw=0.7, ls=":")
a.plot([0.705, 0.8112], [0.8315, 0.8315], color=C["mod"], lw=0.7, ls=":")
a.set_xlim(0.70, 0.86); a.set_ylim(0.73, 0.88)
a.set_xlabel(r"$\sigma_8$"); a.set_ylabel(r"$S_8$")
a.set_title(r"$\sigma_8$ and $S_8$ are the same measurement, "
            "rescaled by 1.025", fontsize=9.5)
a.legend(loc="upper left")
fig.savefig(f"{OUT}/fig2_s8_sigma8.png"); plt.close(fig)

# ============================================================== FIG 3
fig, a = plt.subplots(figsize=(5.8, 4.0))
a.axhspan(0.80, 1.03, color=C["ok"], alpha=0.13, lw=0)
a.loglog(kh, pkB/pk, color=C["alt"], lw=1.7, ls="--",
         label=r"as evaluated previously: $P_{\rm mod}=T\,P$  (non-standard)")
a.loglog(kh, pkA/pk, color=C["mod"], lw=1.9,
         label=r"standard convention: $P_{\rm mod}=T^2 P$")
for kk_ in (0.5, 1.0, 2.0, 3.0):
    a.plot(kk_, np.interp(kk_, kh, pkB/pk), "o", ms=6,
           mfc="white", mec=C["alt"], mew=1.4, zorder=6)
a.axvspan(0.3, 1.5, color=C["grey"], alpha=0.13, lw=0)
a.text(0.67, 0.135, r"$T\equiv1$ here"+"\nby construction", fontsize=7.8,
       color="#555", ha="center")
a.text(0.335, 0.855, "indicative Lyman-"r"$\alpha$"" tolerance",
       fontsize=7.8, color="#1e7a45")
a.annotate("the four sampling points behind\n"
           r'the quoted ratio $=0.891$ — two of them'"\nlie where $T\equiv1$",
           xy=(2.0, 0.866), xytext=(3.4, 1.35), fontsize=7.6, color=C["alt"],
           arrowprops=dict(arrowstyle="->", color=C["alt"], lw=0.8))
a.annotate(r"$-70\%$ at $k=5$", xy=(5, 0.30), xytext=(6.2, 0.52),
           fontsize=7.8, color=C["mod"],
           arrowprops=dict(arrowstyle="->", color=C["mod"], lw=0.8))
a.set_xlim(0.3, 20); a.set_ylim(0.06, 2.0)
a.set_xticks([0.3, 0.5, 1, 2, 3, 5, 10, 20])
a.set_xticklabels(["0.3", "0.5", "1", "2", "3", "5", "10", "20"])
a.set_yticks([0.1, 0.2, 0.5, 1.0])
a.set_yticklabels(["0.1", "0.2", "0.5", "1.0"])
a.minorticks_off()
a.set_xlabel(r"$k\ \ [h\,\mathrm{Mpc}^{-1}]$")
a.set_ylabel(r"$P_{\rm mod}(k)/P_{\Lambda\rm CDM}(k)$")
a.set_title(r"The Lyman-$\alpha$ pass is an artefact of convention and sampling",
            fontsize=9.5)
a.legend(loc="lower left")
fig.savefig(f"{OUT}/fig3_lyman_alpha.png"); plt.close(fig)

# ============================================================== FIG 4
def growth(karr, beta, meff_h, om=OM, amin=1e-3):
    """delta(k,a=1) for G_eff/G = 1 + 2 b^2 k^2/(k^2 + a^2 m^2)."""
    out = []
    for k in karr:
        def rhs(N, y):
            a_ = np.exp(N)
            E2 = om/a_**3 + (1-om)
            oma = om/a_**3/E2
            dlnH = -1.5*oma
            geff = 1 + 2*beta**2 * k**2/(k**2 + a_**2*meff_h**2)
            return [y[1], -(2+dlnH)*y[1] + 1.5*oma*geff*y[0]]
        s = solve_ivp(rhs, [np.log(amin), 0.0], [amin, amin],
                      rtol=1e-8, atol=1e-12, dense_output=True)
        out.append(s.y[0, -1])
    return np.array(out)

kk = np.logspace(-2.3, 1.5, 90)
g0 = growth(kk, 0.0, KC)
fig, ax = plt.subplots(1, 2, figsize=(7.4, 3.5))
a = ax[0]
for bb, ls in [(0.22, "-"), (0.10, "--"), (0.003, ":")]:
    a.semilogx(kk, 1 + 2*bb**2*kk**2/(kk**2 + KC**2), color=C["mod"], ls=ls,
               lw=1.6, label=rf"$\beta={bb}$")
a.axhline(1, color=C["grey"], lw=0.8)
a.axvline(KC, color=C["grey"], lw=0.8, ls=":")
a.text(KC*1.12, 1.008, r"$k=a\,m_{\rm eff}$", fontsize=7.8, color=C["grey"])
a.annotate("saturates at "r"$1+2\beta^2$", xy=(12, 1.093), xytext=(0.9, 1.075),
           fontsize=8.2, color=C["mod"],
           arrowprops=dict(arrowstyle="->", color=C["mod"], lw=0.9))
a.set_xlabel(r"$k\ \ [h\,\mathrm{Mpc}^{-1}]$"); a.set_ylabel(r"$G_{\rm eff}/G$")
a.set_ylim(0.985, 1.11); a.legend(loc="upper left")
a.set_title(r"(a)  $G_{\rm eff}$ from the published Lagrangian", fontsize=9)

b = ax[1]
for bb, ls in [(0.22, "-"), (0.10, "--")]:
    b.semilogx(kk, (growth(kk, bb, KC)/g0)**2 - 1, color=C["mod"], ls=ls,
               lw=1.7, label=rf"radion prediction, $\beta={bb}$")
b.semilogx(kk, np.where(kk < KC, 1.0, (KC/kk)**1.0) - 1, color=C["alt"],
           lw=1.9, label=r"fitted $T^2(k)-1$ (what is needed)")
b.axhline(0, color=C["grey"], lw=0.8)
b.fill_between(kk, 0, 1.3, color=C["mod"], alpha=0.055, lw=0)
b.fill_between(kk, -1.05, 0, color=C["alt"], alpha=0.055, lw=0)
b.text(0.0058, 1.12, "ENHANCEMENT  (theory)", fontsize=8, color=C["mod"])
b.text(0.0058, -0.97, "SUPPRESSION  (data)", fontsize=8, color=C["alt"])
b.annotate("non-zero even at low $k$:\n"
           r"$a\,m_{\rm eff}$ sweeps through all $k$ as $a\to0$",
           xy=(0.011, 0.245), xytext=(0.030, 0.72), fontsize=7.3,
           color="#8b3a2f",
           arrowprops=dict(arrowstyle="->", color="#8b3a2f", lw=0.8))
b.set_xlabel(r"$k\ \ [h\,\mathrm{Mpc}^{-1}]$")
b.set_ylabel(r"$\Delta P/P$  at  $z=0$")
b.set_ylim(-1.05, 1.30)
b.legend(loc="lower left", bbox_to_anchor=(0.015, 0.085))
b.set_title("(b)  Opposite sign, incompatible shape", fontsize=9)
fig.savefig(f"{OUT}/fig4_geff.png"); plt.close(fig)

# ============================================================== FIG 5
fig, a = plt.subplots(figsize=(6.0, 3.1))
bands = [
    (r"required for a 6% shift in $\sigma_8$   ($\beta\simeq0.2$)",
     4.8e-2, 2.0e-1, C["mod"]),
    (r"allowed: Cassini PPN $\gamma$  (conservative floor)",
     1e-18, 1e-5, C["alt"]),
    (r"allowed: MICROSCOPE $\eta<10^{-15}$  (nominal, composition)",
     1e-18, 1e-14, C["ok"]),
]
for i, (lab, lo, hi, col) in enumerate(bands):
    a.barh(i, np.log10(hi)-np.log10(lo), left=np.log10(lo), height=0.46,
           color=col, alpha=0.8, edgecolor=col, lw=0.8)
    a.text(-18.2, i-0.45, lab, va="bottom", ha="left", fontsize=8.2, color=col)
a.plot([np.log10(1e-5), np.log10(4.8e-2)], [0.50, 0.50], color="#444",
       lw=1.0, marker="|", ms=6, mew=1.2)
a.text((np.log10(4.8e-2)+np.log10(1e-5))/2, 0.50,
       r"  $\geq 4$ orders of magnitude  ", fontsize=8.4, ha="center",
       va="center", color="#444",
       bbox=dict(fc="white", ec="none", pad=1.5))
a.set_yticks([]); a.set_xlim(-18.6, 0.6); a.set_ylim(2.75, -0.75)
a.set_xlabel(r"$\log_{10}\beta^2$   (squared dimensionless matter coupling)")
a.set_title(r"The coupling the fit would require is already excluded",
            fontsize=9.5)
fig.savefig(f"{OUT}/fig5_coupling.png"); plt.close(fig)

print("figures written to", OUT)
for f in sorted(os.listdir(OUT)):
    print("  ", f, os.path.getsize(f"{OUT}/{f}")//1024, "kB")
