# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2044/problem/A

import sys

def solve():
    n = int(sys.stdin.readline().strip())
    cnt = 0
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            if i + k == n:
                cnt += 1
    print(cnt)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()