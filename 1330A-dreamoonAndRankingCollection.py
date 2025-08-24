# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        b = [False] * 207
        for val in a:
            b[val] = True
        
        res = 0
        for p in range(1, 207):
            if not b[p]:
                if x > 0:
                    x -= 1
                else:
                    res = p - 1
                    break
        
        if res == 0:
            p = 1
            while True:
                if not b[p]:
                    if x > 0:
                        x -= 1
                    else:
                        res = p - 1
                        break
                p += 1
                
        print(res)

alif()