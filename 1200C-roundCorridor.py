# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1200/problem/C

import math

def alif():
    n, m, q = map(int, input().split())

    common_divisor = math.gcd(n, m)
    a_vals = [n // common_divisor, m // common_divisor]

    for _ in range(q):
        sx, sy, ex, ey = map(int, input().split())
        block_size_sx = a_vals[sx - 1]
        block_size_ex = a_vals[ex - 1]
        block_sy = (sy - 1) // block_size_sx
        block_ey = (ey - 1) // block_size_ex

        if block_sy == block_ey:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()