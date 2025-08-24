# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    binary = format(n, '06b')
    a = list(binary)
    
    x = a[1]
    a[1] = a[5]
    a[5] = x

    x = a[2]
    a[2] = a[3]
    a[3] = x

    res = int("".join(a), 2)
    print(res)

alif()