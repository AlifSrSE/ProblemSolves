# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1249/problem/E

import sys

def alif():
    n, c = map(int, sys.stdin.readline().split())
    a_costs_input = list(map(int, sys.stdin.readline().split()))
    b_costs_input = list(map(int, sys.stdin.readline().split()))
    f = [0] * n
    g = [0] * n
    f[0] = 0
    g[0] = c

    for p in range(1, n):
        f[p] = min(f[p - 1], g[p - 1]) + a_costs_input[p - 1]
        g[p] = min(c + f[p - 1], g[p - 1]) + b_costs_input[p - 1]

    for p in range(n - 2, 0, -1):
        x = min(f[p + 1], g[p + 1]) + a_costs_input[p]
        y = min(c + f[p + 1], g[p + 1]) + b_costs_input[p]
        f[p] = min(f[p], x)
        g[p] = min(g[p], x)

    results = []
    for p in range(n):
        results.append(min(f[p], g[p]))
    
    sys.stdout.write(" ".join(map(str, results)) + "\n")

if __name__ == "__main__":
    alif()