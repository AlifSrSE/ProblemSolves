# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1293/problem/A

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    while t > 0:
        try:
            n, s, k = map(int, sys.stdin.readline().split())
            d = set(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            t -= 1
            continue
        dist = 0
        
        for p in range(n):
            if s + p <= n and s + p not in d:
                dist = p
                break
            if s - p > 0 and s - p not in d:
                dist = p
                break
        
        print(dist)
        t -= 1

if __name__ == "__main__":
    alif()