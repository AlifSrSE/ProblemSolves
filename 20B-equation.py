# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/20/B

import math

def solve():
    a, b, c = map(float, input().split())
    if a == 0:
        if b == 0:
            if c:
                print("0")
            else:
                print("-1")
        else:
            print("1")
            print(f"{ -c / b:.6f}")
    else:
        if a < 0:
            a = -a
            b = -b
            c = -c
        d = b * b - 4 * a * c
        if d < 0:
            print("0")
        elif d == 0:
            print("1")
            print(f"{ -b / (2 * a):.6f}")
        elif d > 0:
            print("2")
            print(f"{(-b - math.sqrt(d)) / (2 * a):.6f}")
            print(f"{(-b + math.sqrt(d)) / (2 * a):.6f}")

solve()