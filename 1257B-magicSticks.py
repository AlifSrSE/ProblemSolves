# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1257/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())
    while t:
        x, y = map(int, sys.stdin.readline().split())
        ans = True
        
        if x == 1:
            ans = (y == 1)
        elif x == 2 or x == 3:
            ans = (y <= 3)
        else:
            pass 
        sys.stdout.write("YES\n" if ans else "NO\n")
        t -= 1

if __name__ == "__main__":
    alif()