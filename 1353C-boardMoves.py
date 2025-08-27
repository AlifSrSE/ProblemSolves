# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        k = n // 2
        result = 8 * k * (k + 1) * (2 * k + 1) // 6
        print(result)

if __name__ == "__main__":
    alif()