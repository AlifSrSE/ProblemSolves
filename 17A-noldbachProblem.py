# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/17/A

import math

def solve():
    n, k = map(int, input().split())

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 2):
        if not prime[i]:
            continue
        for j in range(2 * i, n + 1, i):
            prime[j] = False

    primes = [i for i in range(2, n + 1) if prime[i]]

    total = 0
    for i in range(2, len(primes)):
        for j in range(i - 1):
            if primes[j] + primes[j + 1] + 1 == primes[i]:
                total += 1

    if total >= k:
        print("YES")
    else:
        print("NO")

solve()