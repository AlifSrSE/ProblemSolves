# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1262/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        mn = float('inf')
        mx = -float('inf')
        
        n = int(sys.stdin.readline())
        for _ in range(n):
            left, right = map(int, sys.stdin.readline().split())
            mn = min(mn, right)
            mx = max(mx, left)
        sys.stdout.write(f"{max(0, mx - mn)}\n")

if __name__ == "__main__":
    alif()