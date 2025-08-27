# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())

        if n <= 1:
            print(0)
        elif n == 2:
            print(m)
        else:
            print(2 * m)

if __name__ == "__main__":
    alif()