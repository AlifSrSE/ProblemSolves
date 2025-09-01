# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, k = map(int, sys.stdin.readline().split())
        x = n // k
        a = min(x, m)
        b = (m - a + (k - 2)) // (k - 1)
        res = a - b
        print(res)

if __name__ == "__main__":
    alif()