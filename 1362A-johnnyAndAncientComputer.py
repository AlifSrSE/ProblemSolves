# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    a, b = map(int, sys.stdin.readline().split())

    if a > b:
        a, b = b, a

    if b % a != 0:
        print(-1)
        return

    res = 0
    ratio = b // a

    while ratio % 8 == 0:
        ratio //= 8
        res += 1
    while ratio % 4 == 0:
        ratio //= 4
        res += 1
    while ratio % 2 == 0:
        ratio //= 2
        res += 1

    if ratio == 1:
        print(res)
    else:
        print(-1)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
