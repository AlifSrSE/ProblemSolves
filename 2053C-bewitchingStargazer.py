# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2053/problem/C

class Outcome:
    def __init__(self, lucky, size):
        self.lucky = lucky
        self.size = size

def search(cache, k, n):
    if n < k:
        return Outcome(0, 0)

    if n not in cache:
        sub_outcome = search(cache, k, n // 2)

        if n % 2 == 0:
            cache[n] = Outcome(
                sub_outcome.lucky + (sub_outcome.lucky + n // 2 * sub_outcome.size),
                sub_outcome.size * 2
            )
        else:
            cache[n] = Outcome(
                sub_outcome.lucky + (sub_outcome.lucky + (n // 2 + 1) * sub_outcome.size) + (n // 2 + 1),
                sub_outcome.size * 2 + 1
            )

    return cache[n]

def solve(n, k):
    cache = {}
    return search(cache, k, n).lucky

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))