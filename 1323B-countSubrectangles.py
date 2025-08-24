# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n, m, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    for p in range(1, n):
        if a[p] == 1:
            a[p] += a[p - 1]
    for p in range(1, m):
        if b[p] == 1:
            b[p] += b[p - 1]
    count = 0

    for p in range(n):
        u = p + 1
        if k % u == 0:
            v = k // u
            w = 0
            z = 0

            for q in range(n):
                if a[q] >= u:
                    w += 1
            for q in range(m):
                if b[q] >= v:
                    z += 1
            count += w * z
            
    print(count)    
alif()