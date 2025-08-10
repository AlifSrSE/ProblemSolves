# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1284/problem/A

import sys

def alif():
    try:
        n, m = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().split()
        t = sys.stdin.readline().split()
        q = int(sys.stdin.readline())

        for _ in range(q):
            y = int(sys.stdin.readline())
            y -= 1
            result = s[y % n] + t[y % m]
            sys.stdout.write(result + "\n")

    except (IOError, ValueError):
        return

if __name__ == "__main__":
    alif()