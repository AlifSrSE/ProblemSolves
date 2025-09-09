# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s, a, b = n, 0, 0
    while s % 2 == 0:
        a += 1
        s //= 2
    while s % 3 == 0:
        b += 1
        s //= 3
    if s != 1 or b < a:
        print(-1)
    else:
        print(2 * b - a)
