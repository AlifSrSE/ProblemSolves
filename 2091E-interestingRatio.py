# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/E
 
N = 10**7
prime = [True] * N
primes = []

prime[0] = prime[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, N, i):
            prime[j] = False

for i in range(2, N):
    if prime[i]:
        primes.append(i)

def mySolve():
    n = int(input())
    ans = 0
    for p in primes:
        if p > n:
            break
        ans += n // p
    print(ans)


t = int(input())
for _ in range(t):
    mySolve()