# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/C

import sys

def solve():
    a, b = map(int, sys.stdin.readline().split())
    dist = b - a
    left, right = 1, dist + 7
    res = 1
    while left <= right:
        mid = (left + right) // 2
        tst = mid * (mid - 1) // 2
        if tst <= dist:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    sys.stdout.write(str(res) + "\n")

try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
except ValueError:
    pass