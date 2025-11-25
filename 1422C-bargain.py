# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

MOD = 10**9 + 7

def main():
    import sys
    s = sys.stdin.readline().strip()
    m = len(s)
    pow10 = [1] * (m + 1)

    for i in range(1, m + 1):
        pow10[i] = (pow10[i-1] * 10) % MOD
    S = [0] * (m + 1)

    for r in range(1, m + 1):
        S[r] = (S[r-1] + r * pow10[r-1]) % MOD
    res = 0

    for i, ch in enumerate(s):
        d = ord(ch) - 48
        r = m - i - 1
        contrib_pref = d * S[r] % MOD
        left_sub_count = i * (i + 1) // 2
        contrib_suf = d * pow10[r] % MOD * (left_sub_count % MOD) % MOD
        res = (res + contrib_pref + contrib_suf) % MOD
    print(res)

if __name__ == "__main__":
    main()
