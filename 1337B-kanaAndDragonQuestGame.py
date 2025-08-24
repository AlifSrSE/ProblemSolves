# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x, n, m = map(int, sys.stdin.readline().split())
        while n > 0 and x > 20:
            x = (x // 2) + 10
            n -= 1

        while m > 0 and x > 0:
            x -= 10
            m -= 1

        if x <= 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()