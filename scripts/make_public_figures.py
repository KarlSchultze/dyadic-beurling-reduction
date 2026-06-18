"""Generate public-safe figures for dyadic-beurling-reduction GitHub Pages.

These figures intentionally avoid any material from later contradiction-proof research.
They visualize only the already-public dyadic-to-integer reduction and a finite-block
numerical model for the earlier reversal-across-the-decimal series G(s).
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[1] / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def rho(x: np.ndarray) -> np.ndarray:
    return x - np.floor(x)


def reciprocal_atom(x: np.ndarray, n: int) -> np.ndarray:
    # Endpoint form from the public note under x = 1/y.
    return rho(1.0 / (n * x)) - (1.0 / n) * rho(1.0 / x)


def make_reciprocal_atoms() -> None:
    x = np.linspace(0.035, 1.0, 4000)
    plt.figure(figsize=(8.5, 4.7))
    for n in (2, 3, 5):
        plt.plot(x, reciprocal_atom(x, n), linewidth=1.0, label=f"n={n}")
    plt.axhline(0, linewidth=0.8)
    plt.title("Integer reciprocal Beurling atoms")
    plt.xlabel("x in (0,1]")
    plt.ylabel(r"$\rho(1/(nx)) - n^{-1}\rho(1/x)$")
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(OUT / "reciprocal_atoms.svg", format="svg")
    plt.savefig(OUT / "reciprocal_atoms.png", dpi=180)
    plt.close()


def reverse_digits_fixed_width(n: int, width: int) -> int:
    return int(str(n).zfill(width)[::-1])


def reversal_terms(max_digits: int = 4) -> np.ndarray:
    vals = []
    for k in range(1, max_digits + 1):
        start = 1 if k == 1 else 10 ** (k - 1)
        stop = 10 ** k
        scale = 10 ** k
        for n in range(start, stop):
            rev = reverse_digits_fixed_width(n, k)
            # 0.rev_k(n) divided by n, i.e. rev_k(n)/(10^k n).
            vals.append(rev / (scale * n))
    vals = np.asarray(vals, dtype=float)
    vals = vals[vals > 0]
    return vals


def finite_G(s: np.ndarray, log_terms: np.ndarray) -> np.ndarray:
    # Finite entire proxy G_K(s)=sum exp(s log(a_n)).
    # Evaluate in chunks to avoid high peak memory.
    flat_s = np.ravel(s)
    out = np.zeros(flat_s.shape, dtype=np.complex128)
    chunk = 2000
    for i in range(0, len(log_terms), chunk):
        L = log_terms[i:i+chunk]
        out += np.exp(flat_s[:, None] * L[None, :]).sum(axis=1)
    return out.reshape(s.shape)


def make_g_real_axis() -> None:
    terms = reversal_terms(4)
    log_terms = np.log(terms)
    sigma = np.linspace(-1.0, 3.0, 420)
    s = sigma.astype(np.complex128)
    y = finite_G(s, log_terms).real
    plt.figure(figsize=(8.5, 4.7))
    plt.plot(sigma, np.sign(y) * np.log10(1 + np.abs(y)), linewidth=1.6)
    plt.axvline(1.0, linestyle="--", linewidth=1.0)
    plt.axhline(0, linewidth=0.8)
    plt.title(r"Finite-block model $G_4(\sigma)$ across the convergence boundary")
    plt.xlabel(r"real parameter $\sigma$")
    plt.ylabel(r"signed $\log_{10}(1+|G_4(\sigma)|)$")
    plt.tight_layout()
    plt.savefig(OUT / "g_finite_block_real_axis.svg", format="svg")
    plt.savefig(OUT / "g_finite_block_real_axis.png", dpi=180)
    plt.close()


def make_g_heatmap() -> None:
    terms = reversal_terms(3)
    log_terms = np.log(terms)
    sigmas = np.linspace(-1.0, 3.0, 220)
    ts = np.linspace(-28.0, 28.0, 240)
    S = sigmas[None, :] + 1j * ts[:, None]
    G = finite_G(S, log_terms)
    Z = np.log10(1.0 + np.abs(G))
    plt.figure(figsize=(8.5, 5.2))
    extent = [sigmas.min(), sigmas.max(), ts.min(), ts.max()]
    im = plt.imshow(Z, origin="lower", aspect="auto", extent=extent)
    plt.axvline(1.0, linestyle="--", linewidth=1.0)
    plt.colorbar(im, label=r"$\log_{10}(1+|G_3(s)|)$")
    plt.title(r"Numerical finite-block continuation picture for $G_3(s)$")
    plt.xlabel(r"$\sigma=\Re(s)$")
    plt.ylabel(r"$t=\Im(s)$")
    plt.tight_layout()
    plt.savefig(OUT / "g_finite_block_heatmap.png", dpi=200)
    plt.close()


def make_projection_dichotomy_svg() -> None:
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="520" viewBox="0 0 1100 520" role="img" aria-labelledby="title desc">
  <title id="title">Projection dichotomy flow</title>
  <desc id="desc">A public-safe diagram of the dyadic residual dichotomy from the deployed note.</desc>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#333" />
    </marker>
    <style>
      .box{fill:#f8f8fb;stroke:#333;stroke-width:2;rx:18;ry:18}
      .small{font: 20px system-ui, -apple-system, Segoe UI, sans-serif; fill:#111}
      .math{font: italic 24px Georgia, serif; fill:#111}
      .caption{font: 18px system-ui, -apple-system, Segoe UI, sans-serif; fill:#333}
      .arrow{stroke:#333;stroke-width:2.2;fill:none;marker-end:url(#arrow)}
    </style>
  </defs>
  <rect x="40" y="60" width="300" height="140" class="box"/>
  <text x="190" y="110" text-anchor="middle" class="small">Dyadic residual</text>
  <text x="190" y="153" text-anchor="middle" class="math">x_Q = ||r_Q||²</text>

  <rect x="400" y="40" width="300" height="175" class="box"/>
  <text x="550" y="90" text-anchor="middle" class="small">Alternative A</text>
  <text x="550" y="134" text-anchor="middle" class="math">x_Q ≤ 4 d_Q²</text>
  <text x="550" y="174" text-anchor="middle" class="caption">controlled by integer endpoint</text>

  <rect x="760" y="40" width="300" height="175" class="box"/>
  <text x="910" y="90" text-anchor="middle" class="small">Alternative B</text>
  <text x="910" y="134" text-anchor="middle" class="math">x_Q − x_lcm ≥ x_Q²/4</text>
  <text x="910" y="174" text-anchor="middle" class="caption">strict refinement drop</text>

  <rect x="395" y="300" width="670" height="135" class="box"/>
  <text x="730" y="350" text-anchor="middle" class="small">Public endpoint</text>
  <text x="730" y="392" text-anchor="middle" class="caption">If the integer Beurling / Báez-Duarte distance tends to zero,</text>
  <text x="730" y="422" text-anchor="middle" class="caption">then the dyadic residuals tend to zero along the refinement chain.</text>

  <path d="M340,130 C365,130 375,128 400,128" class="arrow"/>
  <path d="M700,128 C725,128 735,128 760,128" class="arrow"/>
  <path d="M550,215 C555,260 610,285 665,300" class="arrow"/>
  <path d="M910,215 C905,260 850,285 795,300" class="arrow"/>
</svg>'''
    (OUT / "projection_dichotomy.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    make_reciprocal_atoms()
    make_g_real_axis()
    make_g_heatmap()
    make_projection_dichotomy_svg()
    print(f"Wrote figures to {OUT}")
