# Higher-Order Residue Deficits in Legendre Intervals

**Titan Project — Paper XII**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

We generalize the Spin Asymmetry Theorem ([Paper IX](https://zenodo.org/records/18706876)) from quadratic residues to **arbitrary $k$-th power residues**.

**Theorem:** Let $p = 2n-1$ be prime with $k \mid (p-1)$. The $k$-th power residue symbol partitions the nonzero residues into $k$ classes. The interior of the Legendre interval $[(n-1)^2, n^2]$ exhibits a **universal phase deficit**: the class containing the missing residue $r \equiv n^2 \pmod{p}$ has exactly one fewer representative than each of the other $k-1$ classes.

This is a direct corollary of the punctured residue system from Paper IX.

**Verified** for $k = 2, 3, 4, 5$ across all qualifying primes up to $n = 1000$ (100.00% rigidity for each $k$).

## Repository Structure

```
├── paper/
│   ├── Cubic_Phase.tex               # LaTeX source (4 pages)
│   └── Cubic_Phase.pdf               # Compiled PDF
├── scripts/
│   ├── cubic_spin_scanner.py          # Cubic phase display
│   └── higher_order_stress_test.py    # Full k=2,3,4,5 verification
├── LICENSE
└── README.md
```

## Quick Start

```bash
pip install sympy
python scripts/higher_order_stress_test.py --limit 1000
```

## Companion Papers (Titan Project)

| # | Title | Link |
|---|-------|------|
| IX | Quadratic Residue Asymmetry in Legendre Intervals | [Zenodo:18706876](https://zenodo.org/records/18706876) |
| X | Oppermann's Parity Law | [Zenodo:18707265](https://zenodo.org/records/18707265) |
| XI | Radical Compression in Maximal Prime Gaps | [Zenodo:18713375](https://zenodo.org/records/18713375) |
| **XII** | **Higher-Order Residue Deficits (this repo)** | Zenodo (forthcoming) |

## Citation

```bibtex
@article{chen2026cubic,
  author  = {Ruqing Chen},
  title   = {Higher-Order Residue Deficits in Legendre Intervals},
  year    = {2026},
  note    = {Titan Project Paper XII}
}
```

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
