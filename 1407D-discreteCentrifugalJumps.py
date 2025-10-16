# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
def alif():
    n = int(input())
    h = list(map(int, input().split()))
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            valid = True
            if j == i + 1:
                dp[j] = min(dp[j], dp[i] + 1)
                continue
            min_h = min(h[i], h[j])
            max_h = max(h[i], h[j])
            for k in range(i + 1, j):
                if not (h[k] < min_h or h[k] > max_h):
                    valid = False
                    break
            if valid:
                dp[j] = min(dp[j], dp[i] + 1)
    
    print(dp[n - 1])

alif()