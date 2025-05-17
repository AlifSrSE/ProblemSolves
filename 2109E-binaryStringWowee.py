# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2109/problem/E

MOD = 998244353
MAX = 501

fact = [1] * MAX
invfact = [1] * MAX

def power(a, b):
    res = 1
    a %= MOD
    while b > 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res

def modinv(a):
    return power(a, MOD - 2)

def comb(n, k):
    if k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] % MOD * invfact[n - k]) % MOD

def init_factorials():
    fact[0] = invfact[0] = 1
    for i in range(1, MAX):
        fact[i] = (fact[i - 1] * i) % MOD
        invfact[i] = modinv(fact[i])

def alif():
    n, k = map(int, input().split())
    s = input().strip()
    
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for i in range(n - 1, -1, -1):
        ndp = [0] * (k + 1)
        for len_ in range(k + 1):
            if dp[len_] == 0:
                continue
            for cnt in range(k - len_ + 1):
                T = len_ + cnt
                even = (T + 1) // 2
                odd = T // 2
                parity = int(s[i])
                P = even if parity == 0 else odd
                ways = comb(P, cnt)
                ndp[T] = (ndp[T] + dp[len_] * ways % MOD) % MOD
        dp = ndp
    
    print(dp[k])

init_factorials()

t = int(input())
for _ in range(t):
    alif()