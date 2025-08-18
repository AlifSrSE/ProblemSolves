# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1316/problem/C

import sys

def alif():
    n, m, p = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    index_a = -1

    for i in range(n):
        if a[i] % p != 0:
            index_a = i
            break

    index_b = -1
    for j in range(m):
        if b[j] % p != 0:
            index_b = j
            break
    print(index_a + index_b)
alif()