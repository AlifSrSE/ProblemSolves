# Author: AlifSrSE

import sys

def solve(n):
    return len(n)

t = int(sys.stdin.readline())
for _ in range(t):
    n = sys.stdin.readline().strip()
    print(solve(n))
