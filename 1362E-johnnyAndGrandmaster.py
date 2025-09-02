# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif():
    MOD = 1000000007
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        k = list(map(int, input().split()))
        if p == 1:
            print((n % 2) % MOD)
            continue
        powers = sorted([pow(p, ki, MOD * p) for ki in k], reverse=True)
        if n == 1:
            print(powers[0] % MOD)
            continue
        i = 0
        total_diff = 0
        while i < n:
            curr = powers[i]
            j = i + 1
            while j < n and curr > 0:
                curr = (curr - powers[j]) % (MOD * p)
                j += 1
                if curr == 0:
                    break
            if curr > 0:
                total_diff = (total_diff + curr) % (MOD * p)
                i = j
            else:
                i = j
        print(total_diff % MOD)

alif()