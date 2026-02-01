# Author: AlifSrSE

import sys

def solve(x):
    result = 0
    pos = 0
    while pos != x and pos <= x + 1:
        result += 1
        pos += result
    return result

t = int(sys.stdin.readline())
for _ in range(t):
    x = int(sys.stdin.readline())
    print(solve(x))
