# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2070/problem/B

import sys

def solve():
    n, x, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    
    init = x
    for i in range(n):
        if init == 0:
            break
        if s[i] == 'L':
            init -= 1
        else:
            init += 1
        k -= 1
    
    ans = 0
    if init == 0 and k >= 0:
        ans = 1
    
    initt = 0
    cnt = 0
    for i in range(n):
        if s[i] == 'L':
            initt -= 1
        else:
            initt += 1
        cnt += 1
        if initt == 0:
            break
    
    if initt == 0 and init == 0:
        ans += (k // cnt)
    
    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()