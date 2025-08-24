# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        first_one = n
        first_minus_one = n
        
        for i in range(n):
            if a[i] == 1 and first_one == n:
                first_one = i
            if a[i] == -1 and first_minus_one == n:
                first_minus_one = i
        
        possible = True
        for i in range(n):
            if b[i] > a[i]:
                if first_one > i:
                    possible = False
                    break

            if b[i] < a[i]:
                if first_minus_one > i:
                    possible = False
                    break
        
        if possible:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
        t -= 1

alif()