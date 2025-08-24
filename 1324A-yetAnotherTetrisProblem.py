# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        is_possible = True
        
        for i in range(1, n):
            if (a[0] % 2) != (a[i] % 2):
                is_possible = False
                break
        if is_possible:
            print("YES")
        else:
            print("NO")

alif()                                             