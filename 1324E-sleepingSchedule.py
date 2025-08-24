# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def alif(n, h, l, r, a):
    dp = [[-1] * h for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(n):
        for t in range(h):
            if dp[i][t] == -1:
                continue
            next_time = (t + a[i]) % h
            good = 1 if l <= next_time <= r else 0
            dp[i + 1][next_time] = max(dp[i + 1][next_time], dp[i][t] + good)
            
            next_time = (t + a[i] - 1) % h
            good = 1 if l <= next_time <= r else 0
            dp[i + 1][next_time] = max(dp[i + 1][next_time], dp[i][t] + good)
    return max(dp[n])

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))
print(alif(n, h, l, r, a))