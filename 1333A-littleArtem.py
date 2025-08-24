# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        r, c = map(int, sys.stdin.readline().split())
        
        for row in range(r):
            for col in range(c):
                if row == 0 and col == 0:
                    sys.stdout.write('W')
                else:
                    sys.stdout.write('B')
            sys.stdout.write('\n')
        
        t -= 1

alif()