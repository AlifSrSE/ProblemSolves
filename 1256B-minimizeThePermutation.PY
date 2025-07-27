# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1256/problem/B

import sys

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        start = 0
        b = []

        while start < n:
            mn = a[start]
            nxt = start
            for p in range(start, n):
                if a[p] < mn:
                    mn = a[p]
                    nxt = p
                    
            b.append(mn)
            for p in range(start, nxt):
                b.append(a[p])
            
            if nxt > start:
                a[nxt] = a[nxt - 1]
                start = nxt
            else:
                start += 1
        sys.stdout.write(" ".join(map(str, b[:n])) + "\n")

if __name__ == "__main__":
    alif()