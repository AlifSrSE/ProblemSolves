# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1257/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    while t:
        n, x, a, b = map(int, sys.stdin.readline().split())
        d = abs(b - a)
        d += x
        d = min(d, n - 1)
        sys.stdout.write(f"{d}\n")
        t -= 1

if __name__ == "__main__":
    alif()