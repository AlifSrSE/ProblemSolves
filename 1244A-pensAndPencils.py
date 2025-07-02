# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1244/problem/A

import math

def alif():
    t = int(input())

    for _ in range(t):
        a, b, c, d, k = map(int, input().split())
        x = (a + c - 1) // c
        y = (b + d - 1) // d

        if x + y > k:
            print("-1")
        else:
            print(f"{x} {y}")

if __name__ == "__main__":
    alif()