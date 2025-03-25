# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2043/problem/B

import math
import sys

def solve():
    n, d = map(int, input().split())
    ans = [1]
    if n >= 3 or d % 3 == 0:
        ans.append(3)
    if d == 5:
        ans.append(5)
    if d % 7 == 0 or n >= 3:
        ans.append(7)
    if d % 9 == 0 or n >= 6 or (n >= 3 and d % 3 == 0):
        ans.append(9)
    print(*ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()