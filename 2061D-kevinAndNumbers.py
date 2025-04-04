# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from collections import Counter

MOD = 998244353 
input = sys.stdin.readline  

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    
    freq = Counter(A)
    
    def can(x, freq=freq):
        if freq.get(x, 0) > 0:
            freq[x] -= 1
            if freq[x] == 0:
                del freq[x]
            return True
        
        if x == 1:
            return False
        
        p = x >> 1
        q = x - p
        
        return can(p) and can(q)
    
    B = list(map(int, input().split()))
    okay = all(can(x) for x in B) 
    
    print("Yes" if okay and not freq else "No")  

t = int(input())
for _ in range(t):
    solve()