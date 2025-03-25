# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2044/problem/C

import sys

def solve():
    m, a, b, c = map(int, sys.stdin.readline().strip().split())
    
    ans = 0
    if a >= m:
        ans += m
    else:
        ans += a
        d = m - a
        ans += min(d, c)
        c -= min(d, c)
    
    if b >= m:
        ans += m
    else:
        ans += b
        d = m - b
        ans += min(d, c)
        c -= min(d, c)
    
    print(ans)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()