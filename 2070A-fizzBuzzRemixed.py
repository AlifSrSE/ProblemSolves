# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2070/problem/A

import sys
import math

def solve():
    n = int(sys.stdin.readline())
    if n < 3:
        print(n + 1)
        return
    d = (n - 3) // 15 + (1 if (n - 3) % 15 else 0)
    ans = d * 3
    if d * 15 <= n:
        ans += 1
    if d * 15 + 1 <= n:
        ans += 1
    if d * 15 + 2 <= n:
        ans += 1
    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()