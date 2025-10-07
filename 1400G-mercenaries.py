# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif():
    MOD = 998244353
    n, m = map(int, input().split())
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    invfact = [0] * (n + 1)
    invfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % MOD
    
    def binom(nn, kk):
        if kk < 0 or kk > nn:
            return 0
        return fact[nn] * invfact[kk] % MOD * invfact[nn - kk] % MOD
    
    limits = []
    for _ in range(n):
        l, r = map(int, input().split())
        limits.append((l, r))
    
    hate_pairs = []
    for _ in range(m):
        a, b = map(int, input().split())
        hate_pairs.append((a - 1, b - 1))
    
    max_k = n
    count_k = [0] * (max_k + 1)
    
    for i in range(n):
        l, r = limits[i]
        if l <= max_k:
            count_k[l] += 1
            if r + 1 <= max_k:
                count_k[r + 1] -= 1
    
    for i in range(1, max_k + 1):
        count_k[i] += count_k[i - 1]
    
    result = 0
    
    for k in range(1, max_k + 1):
        c = count_k[k]
        if c == 0:
            continue
        total = binom(c, k)
        
        for mask in range(1, 1 << m):
            valid = True
            for i in range(m):
                if mask & (1 << i):
                    a, b = hate_pairs[i]
                    la, ra = limits[a]
                    lb, rb = limits[b]
                    if not (la <= k <= ra and lb <= k <= rb):
                        valid = False
                        break
            if not valid:
                continue
            
            forbidden = set()
            for i in range(m):
                if mask & (1 << i):
                    a, b = hate_pairs[i]
                    forbidden.add(a)
                    forbidden.add(b)
            f = len(forbidden)
            
            if f > k:
                contrib = 0
            else:
                contrib = binom(c - f, k - f)
            
            pop = bin(mask).count('1')
            sign = 1 if pop % 2 == 0 else MOD - 1
            total = (total + sign * contrib) % MOD
        
        result = (result + total) % MOD
    
    print(result)

alif()
