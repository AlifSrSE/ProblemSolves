# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2048/problem/B

import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = [0] * n
    x = 1
    for i in range(k, n + 1, k):
        a[i - 1] = x
        x += 1
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            a[i] = x
            x += 1
    print(*a)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()