# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    a = int(sys.stdin.readline())
    x = 1
    y = a
    p = 2
    while p * p <= a:
        if a % p == 0:
            x = p
            y = a // p
            break
        p += 1
    
    print(str(x) + str(y))

alif()