# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    a = []
    current_max = 0
    
    for val_b in b:
        val_a = val_b + current_max
        a.append(val_a)
        if val_a > current_max:
            current_max = val_a
    
    print(*a)

alif()