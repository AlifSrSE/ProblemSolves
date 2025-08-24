# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        found = False
        first_occurrence = {}
        
        for i in range(n):
            if a[i] in first_occurrence:
                if i - first_occurrence[a[i]] >= 2:
                    found = True
                    break
            else:
                first_occurrence[a[i]] = i
        if found:
            print("YES")
        else:
            print("NO")

alif()