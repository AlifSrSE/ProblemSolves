# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2109/problem/B

import math

def cl2(xi):
    if xi <= 1:
        return 0
    return math.floor(math.log2(xi - 1)) + 1

def alif():
    ni, mi, ai, bi = map(int, input().split())
    dai = min(ai, ni - ai + 1)
    dbi = min(bi, mi - bi + 1)
    chi = 1 + cl2(mi) + cl2(dai)
    cvi = 1 + cl2(ni) + cl2(dbi)
    print(min(chi, cvi))

t = int(input())
for _ in range(t):
    alif()