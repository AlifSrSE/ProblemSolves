# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1307/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, d = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        s = a[0]
        for p in range(1, n):
            if d == 0:
                break
            
            moves = min(a[p], d // p)
            s += moves
            d -= moves * p
        
        print(s)

if __name__ == "__main__":
    alif()