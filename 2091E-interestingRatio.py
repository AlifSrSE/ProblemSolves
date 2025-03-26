# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/E
 
MAX_N = 10007
primes = []
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, MAX_N + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for p in primes:
        if p > n:
            break
        count += n // p
    print(count)