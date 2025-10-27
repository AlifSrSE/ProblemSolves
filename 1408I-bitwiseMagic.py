# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    MOD = 998244353
    sys.setrecursionlimit(200000)

    def power(a, b):
        res = 1
        a %= MOD
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % MOD
            a = (a * a) % MOD
            b //= 2
        return res

    def inverse(n):
        return power(n, MOD - 2)
    MAX_K = 16
    fact = [1] * (MAX_K + 1)
    inv_fact = [1] * (MAX_K + 1)

    for i in range(1, MAX_K + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    inv_fact[MAX_K] = inverse(fact[MAX_K])
    for i in range(MAX_K - 1, 1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def poly_mul(P1, P2, k_limit):
        P_new = [0] * (k_limit + 1)
        for i in range(len(P1)):
            if P1[i] == 0:
                continue
            for j in range(len(P2)):
                if P2[j] == 0:
                    continue
                if i + j <= k_limit:
                    P_new[i + j] = (P_new[i + j] + P1[i] * P2[j]) % MOD
        return P_new

    def poly_power(P, exp, k_limit):
        res = [0] * (k_limit + 1)
        res[0] = 1
        P_curr = P[:]
        
        if len(P_curr) > k_limit + 1:
            P_curr = P_curr[:k_limit + 1]

        while exp > 0:
            if exp % 2 == 1:
                res = poly_mul(res, P_curr, k_limit)
            P_curr = poly_mul(P_curr, P_curr, k_limit)
            exp //= 2
        return res
    
    n, k, c = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    A_xor = 0
    for val in a:
        A_xor ^= val
    
    N_pow_k_inv = inverse(power(n, k))
    M = 1 << c
    R_k_coeff = [0] * M
    
    for j in range(M):
        S_j = [0] * (k + 1)
        for t in range(k + 1):
            sign = 1 if (t & j) % 2 == 0 else MOD - 1
            S_j[t] = (inv_fact[t] * sign) % MOD
            
        S_j_pow_n = poly_power(S_j, n, k)
        R_j_k_coeff_unsigned = S_j_pow_n[k]
        sign_A = 1 if (A_xor & j).bit_count() % 2 == 0 else MOD - 1
        R_k_coeff[j] = (R_j_k_coeff_unsigned * sign_A) % MOD
    
    W_k = [0] * M
    inv_M = inverse(M)
    
    for x in range(M):
        sum_val = 0
        for j in range(M):
            sign_x = 1 if (x & j).bit_count() % 2 == 0 else MOD - 1
            
            term = (sign_x * R_k_coeff[j]) % MOD
            sum_val = (sum_val + term) % MOD
        
        W_k[x] = (sum_val * inv_M) % MOD
    final_factor = (fact[k] * N_pow_k_inv) % MOD

    probabilities = [0] * M
    for x in range(M):
        probabilities[x] = (W_k[x] * final_factor) % MOD
        
    print(*(probabilities))

alif()