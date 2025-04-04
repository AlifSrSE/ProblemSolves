# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

MOD = 998244353
MAXN = 500000

fact = [0] * (MAXN + 1)
invfact = [0] * (MAXN + 1)

def modexp(base, exp):
    result = 1
    b = base
    while exp:
        if exp & 1:
            result = (result * b) % MOD
        b = (b * b) % MOD
        exp >>= 1
    return result

def initFactorials():
    fact[0] = 1
    for i in range(1, MAXN + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    invfact[MAXN] = modexp(fact[MAXN], MOD - 2)
    for i in range(MAXN, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % MOD

def main():
    initFactorials()
    
    t = int(input())
    for _ in range(t):
        c = list(map(int, input().split()))
        total = sum(c)
        
        N = total
        oddCount = (N + 1) // 2
        evenCount = N // 2
        
        freqs = [f for f in c if f > 0]
        
        dp = [0] * (oddCount + 1)
        dp[0] = 1
        for f in freqs:
            newdp = [0] * (oddCount + 1)
            for j in range(oddCount + 1):
                if dp[j] == 0:
                    continue
                newdp[j] = (newdp[j] + dp[j]) % MOD
                if j + f <= oddCount:
                    newdp[j + f] = (newdp[j + f] + dp[j]) % MOD
            dp = newdp
        
        validAssignments = dp[oddCount]
        arrangements = (fact[oddCount] * fact[evenCount]) % MOD
        
        denom = 1
        for f in freqs:
            denom = (denom * fact[f]) % MOD
        ans = validAssignments
        ans = (ans * arrangements) % MOD
        ans = (ans * modexp(denom, MOD - 2)) % MOD
        
        print(ans)

if __name__ == '__main__':
    main()
