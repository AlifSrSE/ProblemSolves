# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1304/problem/C

import sys

def alif():
    q = int(sys.stdin.readline())
    while q > 0:
        q -= 1
        n, m = map(int, sys.stdin.readline().split())
        possible = True
        mn = m
        mx = m
        prev = 0
        for p in range(n):
            t, d, u = map(int, sys.stdin.readline().split())
            diff = t - prev
            prev = t
            mn -= diff
            mx += diff
            if mx < d or mn > u:
                possible = False
            mn = max(mn, d)
            mx = min(mx, u)
        
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()