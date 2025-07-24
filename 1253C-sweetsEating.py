# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1253/problem/C

import sys

def alif():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()

    cs = 0
    v = [0] * n
    for p in range(n):
        cs += a[p]
        
        if p >= m:
            v[p] = cs + v[p - m]
        else:
            v[p] = cs
        sys.stdout.write(f"{v[p]} ")
    
    sys.stdout.write("\n")

if __name__ == "__main__":
    alif()