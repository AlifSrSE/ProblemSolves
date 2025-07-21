# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1250/problem/H

import sys

def alif():
    
    q = int(sys.stdin.readline())

    for _ in range(q):
        a = list(map(int, sys.stdin.readline().split()))
        d = 0
        rep = a[0]

        for p in range(9, 0, -1):
            if a[p] <= rep:
                rep = a[p]
                d = p
        
        if d == 0:
            sys.stdout.write("1")
            for _ in range(rep + 1):
                sys.stdout.write(str(d))
        else:
            for _ in range(rep + 1):
                sys.stdout.write(str(d))
        
        sys.stdout.write("\n")

if __name__ == "__main__":
    alif()