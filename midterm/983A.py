import sys
import math


def is_finite(p, q, b):
    g = math.gcd(p, q)
    q //= g

    g = math.gcd(q, b)
    while g != 1:
        while q % g == 0:
            q //= g
        g = math.gcd(q, b)

    return "Finite" if q == 1 else "Infinite"


def main():
    n = int(sys.stdin.readline().strip())
    results = []

    for _ in range(n):
        p, q, b = map(int, sys.stdin.readline().split())
        results.append(is_finite(p, q, b))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()