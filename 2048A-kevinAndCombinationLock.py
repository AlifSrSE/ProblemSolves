# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2048/problem/A

import sys

def solve():
    n = int(sys.stdin.readline().strip())
    if n % 33 == 0:
        print("YES")
    else:
        print("NO")

t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()