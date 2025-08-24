# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        
        if a % b == 0:
            print(0)
        else:
            print(b - (a % b))

alif()