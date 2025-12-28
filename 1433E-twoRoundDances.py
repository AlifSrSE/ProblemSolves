#Author: AlifSrSE

import sys

def P(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res

def C(n, r):
    return P(n) // (P(r) * P(n - r))

def solve(n):
    return C(n - 1, n // 2) * P(n // 2 - 1) * P(n // 2 - 1)

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    n = int(line)
    print(solve(n))

if __name__ == "__main__":
    main()