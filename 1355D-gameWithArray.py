# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n, s = map(int, sys.stdin.readline().split())
    if s < 2 * n:
        print("NO")
    else:
        print("YES")
        for _ in range(n - 1):
            sys.stdout.write("2 ")

        print(s - 2 * (n - 1))
        print("1")

def main():
    alif()

if __name__ == "__main__":
    main()