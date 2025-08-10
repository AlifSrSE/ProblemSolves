# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1285/problem/C

import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def alif():
    try:
        x = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    a = 1
    b = x
    
    for p in range(1, int(math.sqrt(x)) + 1):
        if x % p == 0:
            q = x // p
            if gcd(p, q) == 1:
                a = p
                b = q

    print(a, b)

if __name__ == "__main__":
    alif()