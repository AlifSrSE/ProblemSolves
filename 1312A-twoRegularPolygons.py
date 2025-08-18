# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1312/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        m, n = map(int, sys.stdin.readline().split())
        if m % n == 0:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()