# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1288/problem/A

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return
        
    while t > 0:
        try:
            n, d = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            t -= 1
            continue

        ans = False
        p = 0
        while p * p <= d + 10:
            u = p + (d + p) // (p + 1)
            
            if u <= n:
                ans = True
                break
            p += 1
        
        if ans:
            print("YES")
        else:
            print("NO")
        t -= 1

if __name__ == "__main__":
    alif()