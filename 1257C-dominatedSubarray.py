# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1257/problem/C

import sys

def alif():
    t = int(sys.stdin.readline())
    while t:
        n = int(sys.stdin.readline())
        a_values = list(map(int, sys.stdin.readline().split()))

        res = -1
        f = {}

        for p in range(n):
            a = a_values[p]
            if a in f:
                dist = p - f[a] + 1
                if res == -1 or dist < res:
                    res = dist
            f[a] = p
        
        sys.stdout.write(f"{res}\n")
        t -= 1

if __name__ == "__main__":
    alif()