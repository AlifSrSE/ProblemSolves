# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/D

import sys

def solve():
    n = int(sys.stdin.readline())
    v = [0] + list(map(int, sys.stdin.readline().split()))
    s = sys.stdin.readline().strip()
    w = [False] * (n + 1)
    f = [0] * (n + 1)

    for p in range(1, n + 1):
        if w[p]:
            continue
        u = []
        x = p
        cnt = 0
        while not w[x]:
            u.append(x)
            w[x] = True
            cnt += (s[x - 1] == '0')
            x = v[x]

        for k in range(len(u)):
            f[u[k]] = cnt

    sys.stdout.write(" ".join(map(str, f[1:])) + "\n")

try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
except ValueError:
    pass