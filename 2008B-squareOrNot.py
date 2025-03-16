# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/B

import math
import sys

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    sz = int(math.sqrt(len(s)))
    if sz * sz != len(s):
        sys.stdout.write("No\n")
        return
    
    possible = True
    for row in range(sz):
        for col in range(sz):
            digit = (s[row * sz + col] == '1')
            edge = (row == 0 or row == sz - 1 or col == 0 or col == sz - 1)
            if edge ^ digit:
                possible = False
                break
        if not possible:
            break
    
    sys.stdout.write("Yes\n" if possible else "No\n")

try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
except ValueError:
    pass