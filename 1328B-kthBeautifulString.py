# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
import math

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        
        pos = int((math.sqrt(1 + 8 * k) - 1) / 2)
        remaining = k - pos * (pos + 1) // 2
        
        s = ['a'] * n
        s[n - 1 - (pos + 1)] = 'b'
        s[n - 1 - remaining] = 'b'
        
        print("".join(s))

alif()