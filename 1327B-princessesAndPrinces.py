# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        taken = [False] * (n + 1)
        unmarried_princess = -1
        
        for p in range(1, n + 1):
            line = list(map(int, sys.stdin.readline().split()))
            m = line[0]
            candidates = line[1:]
            
            married = False
            for cand in candidates:
                if not married and not taken[cand]:
                    married = True
                    taken[cand] = True
            
            if not married:
                unmarried_princess = p
        
        if unmarried_princess == -1:
            print("OPTIMAL")
        else:
            unmarried_prince = -1
            for p in range(1, n + 1):
                if not taken[p]:
                    unmarried_prince = p
                    break
            
            print("IMPROVE")
            print(unmarried_princess, unmarried_prince)

alif()