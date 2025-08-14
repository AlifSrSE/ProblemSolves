# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1304/problem/A

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        t = 0
    
    for _ in range(t):
        try:
            x, y, a, b = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue
        dist = y - x
        step = a + b

        if dist % step == 0:
            print(dist // step)
        else:
            print(-1)

if __name__ == "__main__":
    alif()