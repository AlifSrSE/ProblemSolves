# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

MOD = 998244353

def alif():
    n, m, L, R = map(int, input().split())
    N = n * m
    length = R - L + 1

    total = pow(length, N, MOD)

    if N % 2 == 0:
        print(total % MOD)
    else:
        if length % 2 == 0:
            print((total * pow(2, MOD-2, MOD)) % MOD)
        else:
            print(((total + 1) * pow(2, MOD-2, MOD)) % MOD)

if __name__ == "__main__":
    alif()