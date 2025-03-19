# Author : AlifSrSE
# Date : 2025-03-18
# Problem link : https://codeforces.com/contest/1985/problem/B

import math
import sys

def solve():
    n = int(input())
    sum_val = 0
    ans = 2
    for i in range(2, n + 1):
        s = 0
        k = 1
        while i * k <= n:
            s += i * k
            k += 1
        if sum_val < s:
            sum_val = s
            ans = i
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()