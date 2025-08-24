# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        
        s = set()
        left = set()
        mx = 0
        for p in range(n):
            if a[p] in s:
                break
            s.add(a[p])
            mx = max(mx, a[p])
            if len(s) == mx:
                left.add(p)
        
        t = set()
        mx = 0
        ans = []
        for p in range(n - 1, -1, -1):
            if a[p] in t:
                break
            t.add(a[p])
            mx = max(mx, a[p])
            if len(t) == mx and (p - 1) in left:
                ans.append(p)
        
        print(len(ans))
        for p in ans:
            print(p, n - p)

alif()