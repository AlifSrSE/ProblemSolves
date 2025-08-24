# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    MOD = 998244353
    n, k = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    mx = k * n - k * (k - 1) // 2
    positions = []
    threshold = n - k + 1
    
    for i, val in enumerate(p):
        if val >= threshold:
            positions.append(i)
    positions.sort()
    prod = 1

    for i in range(1, len(positions)):
        diff = positions[i] - positions[i-1]
        prod = (prod * diff) % MOD
    print(mx, prod)

alif()