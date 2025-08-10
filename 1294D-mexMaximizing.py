# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1294/problem/D

import sys

def alif():
    try:
        n, x = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return
    
    f = [0] * x
    cnt = 0

    for _ in range(n):
        try:
            y = int(sys.stdin.readline())
        except (IOError, ValueError):
            continue
        f[y % x] += 1

        while f[cnt % x] > (cnt // x):
            cnt += 1
        
        print(cnt)

if __name__ == "__main__":
    alif()