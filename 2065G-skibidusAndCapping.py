# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/G
 
import sys
 
input = sys.stdin.readline
print = sys.stdout.write
 
N = int(2e5 + 5)
primes = []
st = [False] * N
f = [0] * N
 
def init(n):
    global primes, st, f
    for i in range(2, n + 1):
        if not st[i]:
            primes.append(i)
        
        for p in primes:
            if p * i > n:
                break
            st[p * i] = True
            if i % p == 0:
                break
    
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] > n:
                break
            f[primes[i] * primes[j]] = primes[i]
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    ans = 0
    cntp = 0
    cnt = {}
    
    for i in range(n):
        if not st[a[i]]:
            ans += cntp - cnt.get(a[i], 0)
            cntp += 1
        elif f[a[i]]:
            if a[i] // f[a[i]] == f[a[i]]:  
                ans += cnt.get(f[a[i]], 0)
            else:  
                ans += cnt.get(f[a[i]], 0) + cnt.get(a[i] // f[a[i]], 0)
            ans += cnt.get(a[i], 0) + 1
        
        cnt[a[i]] = cnt.get(a[i], 0) + 1
    
    print(str(ans) + "\n")
 
init(int(2e5))
 
t = int(input())
for _ in range(t):
    solve()