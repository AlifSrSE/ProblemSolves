# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1278/B

import sys

def check(d_val, x_val):
    s = x_val * (x_val + 1) // 2
    if d_val > s:
        return False
    
    return (d_val % 2 == s % 2)

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        d = abs(a - b)

        if d == 0:
            sys.stdout.write("0\n")
            continue
        x = 0

        while not check(d, x):
            x += 1
        sys.stdout.write(f"{x}\n")

if __name__ == "__main__":
    alif()