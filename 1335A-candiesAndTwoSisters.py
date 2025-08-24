# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n = int(sys.stdin.readline())
        ans = (n - 1) // 2
        
        sys.stdout.write(str(ans) + '\n')
        t -= 1

alif()