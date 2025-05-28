# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1195/problem/D1

def alif():
    MOD = 998244353
    N_DIGITS = 10
    n = int(input())
    s = [0] * N_DIGITS
    t = [0] * N_DIGITS

    for _ in range(n):
        x = int(input())
        current_digit_idx = 0
        temp_x = x
        while temp_x > 0:
            s[current_digit_idx] = (s[current_digit_idx] + temp_x % 10) % MOD
            current_digit_idx += 1
            temp_x //= 10
        t[current_digit_idx - 1] = (t[current_digit_idx - 1] + 1) % MOD

    ma = 1
    res = 0

    for p in range(N_DIGITS):
        mb = 1
        rem = n

        for q in range(p):
            term = (2 * (mb % MOD) * (t[q] % MOD) * (s[p] % MOD)) % MOD
            res = (res + term) % MOD
            
            mb = (mb * 100) % MOD
            rem = (rem - t[q] + MOD) % MOD

        term_main_s_p = s[p] % MOD
        multiplier_part = (11 * (ma % MOD) * (rem % MOD)) % MOD
        res = (res + (term_main_s_p * multiplier_part) % MOD) % MOD
        
        ma = (ma * 100) % MOD

    print(res)

if __name__ == "__main__":
    alif()