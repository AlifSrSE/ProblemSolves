# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    a, b = map(int, sys.stdin.readline().split())

    if a < b:
        a, b = b, a

    if a >= 2 * b:
        ans = b
    else:
        ans = (a + b) // 3

    sys.stdout.write(str(ans) + "\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()