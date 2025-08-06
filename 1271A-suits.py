# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1271/A

import sys

def alif():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    x = a
    y = min(b, c)
    total_profit = 0

    if e < f:
        num_type2_to_produce = min(y, d)
        total_profit += f * num_type2_to_produce
        d -= num_type2_to_produce
        num_type1_to_produce = min(x, d)
        total_profit += e * num_type1_to_produce
    else:
        num_type1_to_produce = min(x, d)
        total_profit += e * num_type1_to_produce
        d -= num_type1_to_produce
        num_type2_to_produce = min(y, d)
        total_profit += f * num_type2_to_produce
    sys.stdout.write(f"{total_profit}\n")

if __name__ == "__main__":
    alif()