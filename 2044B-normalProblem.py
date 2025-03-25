# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2044/problem/B

import sys

def solve():
    s = sys.stdin.readline().strip()
    result = ""
    for char in reversed(s):
        if char == 'p':
            result += 'q'
        elif char == 'q':
            result += 'p'
        else:
            result += char
    print(result)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    solve()