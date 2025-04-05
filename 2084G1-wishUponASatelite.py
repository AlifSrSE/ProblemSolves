# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from typing import List

N = 1 << 20
MOD = 10**9 + 7

def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    ia = [0] * (n + 1)
    for i in range(1, n + 1):
        if a[i]:
            ia[a[i]] = i
    
    s0 = n // 2
    s1 = (n + 1) // 2
    cnt0 = cnt1 = num = 0
    
    dp = [-10**18] * (n + 1)
    dp[0] = 0
    
    for i in range(n, 0, -1):
        if ia[i]:
            if ia[i] % 2 == 0:
                cnt0 += 1
            else:
                cnt1 += 1
        else:
            num += 1
            for j in range(num, 0, -1):
                dp[j] = max(dp[j], dp[j - 1])
        
        for j in range(num + 1):
            j0 = j + cnt0
            j1 = num - j + cnt1
            dp[j] += j0 * j1
            dp[j] += j0 * (j0 + 1) // 2 + j0 * (s0 - j0)
            dp[j] += j1 * (j1 + 1) // 2 + j1 * (s1 - j1)
    
    print(dp[s0 - cnt0])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()