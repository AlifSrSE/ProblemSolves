# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n = int(sys.stdin.readline())
        plays_prev = 0
        clears_prev = 0
        possible = True

        for _ in range(n):
            plays_curr, clears_curr = map(int, sys.stdin.readline().split())
            if plays_curr < plays_prev:
                possible = False
            if clears_curr < clears_prev:
                possible = False
            if (plays_curr - plays_prev) < (clears_curr - clears_prev):
                possible = False
            
            plays_prev = plays_curr
            clears_prev = clears_curr
        
        if possible:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
        t -= 1

alif()