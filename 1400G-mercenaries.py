# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    MOD = 998244353
    n, m = map(int, input().split())
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
        if count_k[k] == 0:
            continue
        total = (pow(2, count_k[k], MOD) - 1) % MOD

        for mask in range(1, 1 << m):
            forbidden = set()
            for i in range(m):
                if mask & (1 << i):
                    a, b = hate_pairs[i]
                    forbidden.add(a)
                    forbidden.add(b)
            valid_count = count_k[k] - len([i for i in forbidden if limits[i][0] <= k <= limits[i][1]])
            if valid_count < 0:
                continue
            sign = -1 if bin(mask).count('1') % 2 == 1 else 1
            total = (total + sign * (pow(2, valid_count, MOD) - 1)) % MOD
        result = (result + total) % MOD
    
    print(result)

alif()