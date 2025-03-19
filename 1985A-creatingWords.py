# Author : AlifSrSE
# Date : 2025-03-18
# Problem link : https://codeforces.com/contest/1985/problem/A

import math
import sys

def solve():
    a, b = input().split()
    a_list = list(a)
    b_list = list(b)
    a_list[0], b_list[0] = b_list[0], a_list[0]
    print("".join(a_list), "".join(b_list))

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()