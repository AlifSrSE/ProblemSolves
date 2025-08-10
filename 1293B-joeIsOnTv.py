# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1293/problem/B

import sys

def alif():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
    except (IOError, ValueError):
        return
    res = 0.0
    
    for p in range(1, n + 1):
        res += 1.0 / p
        
    print(f"{res:.5f}")

if __name__ == "__main__":
    alif()