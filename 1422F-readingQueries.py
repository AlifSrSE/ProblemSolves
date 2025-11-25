# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
input = sys.stdin.readline
MOD = 10**9 + 7
MAXA = 200000
spf = list(range(MAXA+1))

for i in range(2, int(MAXA**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, MAXA+1, i):
            if spf[j] == j:
                spf[j] = i

def factorize(x):
    f = {}
    while x > 1:
        p = spf[x]
        c = 0
        while x % p == 0:
            x //= p
            c += 1
        f[p] = c
    return f

class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [1] * (n+1)

    def update(self, i, v):
        while i <= self.n:
            self.a[i] = self.a[i] * v % MOD
            i += i & -i

    def query(self, i):
        r = 1
        while i > 0:
            r = r * self.a[i] % MOD
            i -= i & -i
        return r

    def range_prod(self, l, r):
        return self.query(r) * pow(self.query(l-1), MOD-2, MOD) % MOD

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = []

for qi in range(q):
    x, y = map(int, input().split())
    queries.append((x, y, qi))
mapped = [[] for _ in range(n+1)]
last_ans = 0

for x, y, idx in queries:
    l = (last_ans + x) % n + 1
    r = (last_ans + y) % n + 1
    if l > r: l, r = r, l
    mapped[r].append((l, idx))
    last_ans = r

bit = BIT(n)
last = {}
answers = [0] * q

for i in range(1, n+1):
    f = factorize(arr[i-1])

    for p, e in f.items():
        if p in last:
            lpos, le = last[p]
            bit.update(lpos, pow(p, MOD-1-le, MOD))
        bit.update(i, pow(p, e, MOD))
        last[p] = (i, e)

    for l, qi in mapped[i]:
        answers[qi] = bit.range_prod(l, i)

print("\n".join(map(str, answers)))
