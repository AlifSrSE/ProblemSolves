# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, c, d = map(int, sys.stdin.readline().split())
        x, y, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

        ans = True
        x += (b - a)
        if x < x1 or x > x2:
            ans = False
        
        if a == b and x1 == x2 and a > 0:
            ans = False
        
        y += (d - c)
        if y < y1 or y > y2:
            ans = False
        
        if c == d and y1 == y2 and c > 0:
            ans = False
        
        if ans:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")

alif()