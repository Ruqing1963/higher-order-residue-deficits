#!/usr/bin/env python3
"""
higher_order_stress_test.py
===========================
Verify the Higher-Order Residue Deficit Theorem for k-th power
residues (k = 2, 3, 4, 5) across all qualifying Legendre intervals.

Titan Project -- Paper XII, February 2026
Author: Ruqing Chen, GUT Geoservice Inc.
"""

import sympy
import argparse


def stress_test(limit_n, k_values=None):
    if k_values is None:
        k_values = [2, 3, 4, 5]

    print("=" * 70)
    print(f"Higher-Order Residue Deficit: Stress Test (n=2 to {limit_n})")
    print("=" * 70)

    for k in k_values:
        targets = 0
        matches = 0

        for n in range(2, limit_n + 1):
            p = 2 * n - 1
            if not sympy.isprime(p):
                continue
            if (p - 1) % k != 0 or (p - 1) // k < 2:
                continue

            targets += 1
            phases = {}
            for x in range((n - 1) ** 2 + 1, n ** 2):
                res = x % p
                if res == 0:
                    continue
                c = pow(res, (p - 1) // k, p)
                phases[c] = phases.get(c, 0) + 1

            vals = sorted(phases.values())
            if (len(vals) == k
                    and vals[0] == vals[1] - 1
                    and vals.count(vals[1]) == k - 1):
                matches += 1
            else:
                print(f"  FAIL: n={n}, p={p}, k={k}, phases={phases}")

        rate = 100 * matches / targets if targets > 0 else 0
        print(f"k={k}: {matches}/{targets} = {rate:.2f}%")

    print("=" * 70)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Stress test higher-order residue deficits."
    )
    parser.add_argument("--limit", type=int, default=1000,
                        help="Upper bound for n (default: 1000)")
    args = parser.parse_args()
    stress_test(args.limit)
