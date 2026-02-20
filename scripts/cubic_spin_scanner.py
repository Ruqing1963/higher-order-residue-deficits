#!/usr/bin/env python3
"""
cubic_spin_scanner.py
=====================
Scan Legendre intervals for cubic residue phase distribution.
For primes p = 2n-1 with p ≡ 1 (mod 3), displays the three
cubic phase counts and identifies the deficient phase.

Titan Project -- Paper XII, February 2026
Author: Ruqing Chen, GUT Geoservice Inc.
"""

import sympy


def scan_cubic_asymmetry(limit_n):
    print("=" * 80)
    print("Cubic Phase Deficit Scanner: Legendre Intervals")
    print("=" * 80)
    print(f"{'n (p)':<14} | {'Phase 1':<10} | {'Phase w':<10} | "
          f"{'Phase w2':<10} | {'Result'}")
    print("-" * 80)

    for n in range(2, limit_n + 1):
        p = 2 * n - 1
        if sympy.isprime(p) and p % 3 == 1:
            phases = {}
            for x in range((n - 1) ** 2 + 1, n ** 2):
                if x % p == 0:
                    continue
                c = pow(x % p, (p - 1) // 3, p)
                phases[c] = phases.get(c, 0) + 1

            if len(phases) == 3:
                vals = sorted(phases.values())
                deficit = "Deficit found" if vals[0] == vals[1] - 1 else "Anomaly"
            else:
                deficit = "Too small"

            keys = sorted(phases.keys())
            counts = [str(phases.get(k, 0)) for k in keys]

            print(f"n={n:<3} (p={p:<4}) | {'  |  '.join(f'{c:<8}' for c in counts)}"
                  f"  | {deficit}")


if __name__ == '__main__':
    scan_cubic_asymmetry(100)
