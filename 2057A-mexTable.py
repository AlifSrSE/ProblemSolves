# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2057/problem/A

import sys
import math
import collections
import heapq

def solve():
    n, m = map(int, input().split())
    print(max(n, m) + 1)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()