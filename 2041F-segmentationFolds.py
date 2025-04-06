# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
import bisect

sys.setrecursionlimit(1 << 25)
MOD = 998244353
N = 2000010

good_primes = []
vis = [False] * N
sieve = [False] * N
primes = []
minDP = {}

def min_call(l, r):
    sign = (l << 18) | (r - l)
    if sign in minDP:
        return minDP[sign]

    res = r - l
    ways = 1

    bound = (l + r) // 2
    pos = bisect.bisect_right(good_primes, bound) - 1
    if pos >= 0 and good_primes[pos] > l:
        to_res, to_ways = min_call(good_primes[pos], r)
        if to_res < res:
            res, ways = to_res, to_ways
        elif to_res == res:
            ways = (ways + to_ways) % MOD

    bound = (l + r + 1) // 2
    pos = bisect.bisect_left(good_primes, bound)
    if pos < len(good_primes) and good_primes[pos] < r:
        to_res, to_ways = min_call(l, good_primes[pos])
        if to_res < res:
            res, ways = to_res, to_ways
        elif to_res == res:
            ways = (ways + to_ways) % MOD

    minDP[sign] = (res, ways % MOD)
    return minDP[sign]

def main():
    for i in range(2, int(N ** 0.5) + 1):
        if not vis[i]:
            for j in range(i * i, N, i):
                vis[j] = True
    for i in range(2, N):
        if not vis[i]:
            primes.append(i)

    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        minDP.clear()
        good_primes.clear()

        sieve = [False] * (2 * (r - l) + 1)
        for p in primes:
            from_ = ((2 * l + p - 1) // p) * p
            if from_ == p:
                from_ += p
            for j in range(from_, 2 * r + 1, p):
                sieve[j - 2 * l] = True

        for i in range(2 * (r - l) + 1):
            if not sieve[i]:
                good_primes.append(2 * l + i)

        print(min_call(2 * l, 2 * r)[1])

if __name__ == "__main__":
    main()
