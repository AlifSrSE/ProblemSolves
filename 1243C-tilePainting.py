# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1243/problem/C

import math

def alif():
    n = int(input())
    x = -1
    y = -1

    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            if x == -1:
                x = p
            if (p % x != 0) or ((n // p) % x != 0):
                y = p
                break
    res = n
    if x == -1:
        res = n
    elif y == -1:
        res = x
    else:
        res = 1
    
    print(res)

if __name__ == "__main__":
    alif()