# Author: AlifSrSe
# date: 2025-03-25
# https://codeforces.com/problemset/problem/2089/A
 
def solve():
    n = int(input())
    
    minp, primes = sieve(n)
    
    p = max(1, n // 3)
    while minp[p] != p:
        p += 1
    
    a = [p]
    l, r = p, p
    while l > 1 and r < n:
        l -= 1
        r += 1
        a.append(l)
        a.append(r)
    
    for i in range(1, l):
        a.append(i)
    
    for i in range(r + 1, n + 1):
        a.append(i)
    
    print(*a)

def sieve(n):
    minp = [0] * (n + 1)
    primes = []
    
    for i in range(2, n + 1):
        if minp[i] == 0:
            minp[i] = i
            primes.append(i)
        
        for p in primes:
            if i * p > n:
                break
            minp[i * p] = p
            if p == minp[i]:
                break
    return minp, primes

t = int(input())
for _ in range(t):
    solve()