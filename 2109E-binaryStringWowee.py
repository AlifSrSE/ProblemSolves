# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2109/problem/E

MOD = 998244353
MAX = 501

fact = [1] * MAX
invfact = [1] * MAX

def power(ai, bi):
    res = 1
    ai %= MOD
    while bi > 0:
        if bi & 1:
            res = (res * ai) % MOD
        ai = (ai * ai) % MOD
        bi >>= 1
    return res

def modinv(ai):
    return power(ai, MOD - 2)

def comb(ni, ki):
    if ki < 0 or ki > ni:
        return 0
    return (fact[ni] * invfact[ki] % MOD * invfact[ni - ki]) % MOD

def init_factorials():
    fact[0] = invfact[0] = 1
    for i in range(1, MAX):
        fact[i] = (fact[i - 1] * i) % MOD
        invfact[i] = modinv(fact[i])

def alif():
    ni, ki = map(int, input().split())
    si = input().strip()
    
    dp = [0] * (ki + 1)
    dp[0] = 1
    
    for i in range(ni - 1, -1, -1):
        ndp = [0] * (ki + 1)
        for len_ in range(ki + 1):
            if dp[len_] == 0:
                continue
            for cnt in range(ki - len_ + 1):
                TI = len_ + cnt
                even = (TI + 1) // 2
                odd = TI // 2
                parity = int(si[i])
                PI = even if parity == 0 else odd
                ways = comb(PI, cnt)
                ndp[TI] = (ndp[TI] + dp[len_] * ways % MOD) % MOD
        dp = ndp
    
    print(dp[ki])

init_factorials()

ti = int(input())
for _ in range(ti):
    alif()