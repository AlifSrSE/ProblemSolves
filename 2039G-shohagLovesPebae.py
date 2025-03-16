import sys
import math
from collections import defaultdict

class custom_hash:
    def splitmix64(self, x):
        x += 0x9e3779b97f4a7c15
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb
        return x ^ (x >> 31)

    def __call__(self, x):
        import time
        FIXED_RANDOM = time.time_ns()
        return self.splitmix64(x + FIXED_RANDOM)

N = 1000009
T = 10000009
RT = 33333
mod = 998244353

def power(n, k):
    ans = 1 % mod
    while k:
        if k & 1:
            ans = (ans * n) % mod
        n = (n * n) % mod
        k >>= 1
    return ans

def SQRT(n):
    x = int(math.sqrt(n))
    while x * x < n:
        x += 1
    while x * x > n:
        x -= 1
    return x

spf = [0] * T
id_val = [0] * T
DIAMETER = 0
mu = [0] * T
primes = []
prefix_prime_count = [0] * T
prefix_sum_mu = [0] * T

def init():
    global primes
    mu[1] = 1
    for i in range(2, T):
        if spf[i] == 0:
            spf[i] = i
            mu[i] = 0 if i <= DIAMETER else -1
            primes.append(i)
        for j in range(len(primes)):
            if i * primes[j] >= T or primes[j] > spf[i]:
                break
            spf[i * primes[j]] = primes[j]
            if i % primes[j] == 0:
                mu[i * primes[j]] = 0
            else:
                mu[i * primes[j]] = mu[i] * (0 if primes[j] <= DIAMETER else -1)
    primes.insert(0, 0)
    for i in range(1, len(primes)):
        id_val[primes[i]] = i
    for i in range(2, T):
        prefix_prime_count[i] = prefix_prime_count[i - 1] + (spf[i] == i)
    for i in range(1, T):
        prefix_sum_mu[i] = prefix_sum_mu[i - 1] + mu[i]

cnt = [0] * N
m = 0

class GoodNumbers:
    mp = [defaultdict(int) for _ in range(RT << 1)]

    def count_num(self, n, k):
        if k == 0 or n == 0:
            return n
        if primes[k] >= n:
            return 1
        if n < T and 1 * primes[k] * primes[k] > n:
            return 1 + prefix_prime_count[n] - k
        if n in self.mp[k]:
            return self.mp[k][n]
        ans = 0
        if 1 * primes[k] * primes[k] > n:
            x = 0
            for i in range(1,len(primes)):
                if primes[i] > int(math.sqrt(n)):
                    break
                x = i

            ans = self.count_num(n, x) - (k - x)
        else:
            ans = self.count_num(n, k - 1) - self.count_num(n // primes[k], k - 1)
        self.mp[k][n] = ans
        return ans

v = []

class Dirichlet:
    mp = defaultdict(int)

    def p_c(self, n):
        return 0 if n < 1 else 1

    def p_g(self, n):
        return GoodNumbers().count_num(n, v[-1][0])

    def solve(self, x):
        if x < T:
            return prefix_sum_mu[x]
        if x in self.mp:
            return self.mp[x]
        ans = 0
        i = 2
        while i <= x:
            last = x // (x // i)
            ans += self.solve(x // i) * (self.p_g(last) - self.p_g(i - 1))
            i = last + 1
        ans = self.p_c(x) - ans
        self.mp[x] = ans
        return ans

def count_primes(n):
    if n < T:
        return prefix_prime_count[n]
    x = SQRT(n)
    k = 0
    for i in range(1,len(primes)):
        if primes[i] > x:
            break
        k = i
    return GoodNumbers().count_num(n, k) + k - 1

def solve_large():
    total_ways = 1
    primes_under_m = count_primes(m)
    for k, c in v:
        if m <= primes[k]:
            break
        total_ways = (total_ways * power((primes_under_m - k + 1) % mod, c)) % mod
    bad_ways = max(0, primes_under_m - v[-1][0]) % mod
    ans = (total_ways - bad_ways + mod) % mod
    print(ans)

def solve_small():
    ans = 0
    l = 1
    while l <= m:
        x = m // l
        r = m // x
        cur = ((Dirichlet().solve(r) - Dirichlet().solve(l - 1)) % mod + mod) % mod
        if cur:
            mul = 1
            for k, c in v:
                if x <= primes[k]:
                    break
                mul = (mul * power(GoodNumbers().count_num(x, k) % mod, c)) % mod
            ans += (cur * mul) % mod
            ans %= mod
        l = r + 1
    print(ans)

g = [[] for _ in range(N)]
dp = [0] * N
up = [0] * N
pref = [0] * N
suf = [0] * N
mx_d = [0] * N

def dfs(u, p=0):
    dp[u] = 0
    if p:
        if p in g[u]:
            g[u].remove(p)
    for v_val in g[u]:
        if v_val != p:
            dfs(v_val, u)
            dp[u] = max(dp[u], dp[v_val] + 1)

def dfs2(u):
    sz = len(g[u])
    for i in range(sz):
        v_val = g[u][i]
        pref[i] = dp[v_val] + 1
        if i:
            pref[i] = max(pref[i], pref[i - 1])
    for i in range(sz - 1, -1, -1):
        v_val = g[u][i]
        suf[i] = dp[v_val] + 1
        if i + 1 < sz:
            suf[i] = max(suf[i], suf[i + 1])
    for i in range(sz):
        v_val = g[u][i]
        cur = up[u]
        if i:
            cur = max(cur, pref[i - 1])
        if i + 1 < sz:
            cur = max(cur, suf[i + 1])
        up[v_val] = cur + 1
    for v_val in g[u]:
        dfs2(v_val)

def main():
    global DIAMETER, m
    n, m = map(int, sys.stdin.readline().split())
    for _ in range(n - 1):
        u, v_val = map(int, sys.stdin.readline().split())
        g