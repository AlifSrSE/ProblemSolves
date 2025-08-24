# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        
        if n % 2 == k % 2 and n >= k * k:
            print("YES")
        else:
            print("NO")

alif()