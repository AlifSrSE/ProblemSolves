# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1255/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        diff = abs(a - b)
        cnt = (diff // 5) + (1 if diff % 5 > 0 else 0) + (1 if diff % 5 > 2 else 0)
        sys.stdout.write(f"{cnt}\n")

if __name__ == "__main__":
    alif()