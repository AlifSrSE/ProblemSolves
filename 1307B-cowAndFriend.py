# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1307/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        mx = 0
        found = False
        
        for val in a:
            mx = max(mx, val)
            if val == x:
                found = True
        
        if found:
            print(1)
        else:
            if x <= mx:
                print(2)
            else:
                print((x + mx - 1) // mx)

if __name__ == "__main__":
    alif()