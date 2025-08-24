# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        x = sys.stdin.readline().strip()
        
        a = []
        b = []
        diff = False
        
        for p in range(n):
            if x[p] == '0':
                a.append('0')
                b.append('0')
            elif x[p] == '1':
                if diff:
                    a.append('0')
                    b.append('1')
                else:
                    a.append('1')
                    b.append('0')
                    diff = True
            elif x[p] == '2':
                if diff:
                    a.append('0')
                    b.append('2')
                else:
                    a.append('1')
                    b.append('1')

        print("".join(a))
        print("".join(b))

alif()