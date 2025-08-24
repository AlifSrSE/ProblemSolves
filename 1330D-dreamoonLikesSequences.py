# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif(d, m):
    if d == 0:
        return 0
    dp = [0] * (d + 1)
    dp[1] = 1
    for i in range(2, d + 1):
        dp[i] = 1
        for j in range(1, i):
            if (j ^ i) <= d and (j ^ i) > j:
                dp[i] = (dp[i] + dp[j]) % m
    result = 0
    for i in range(1, d + 1):
        result = (result + dp[i]) % m
    return result

t = int(input())
for _ in range(t):
    d, m = map(int, input().split())
    print(alif(d, m))