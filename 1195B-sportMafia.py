# Author : AlifSrSE
# Date : 2025-02-16
# Problem link : https://codeforces.com/contest/1195/problem/B

def find_candies_eaten(n, k):
    for m in range (1, n +1):
        total_candies_put = m * (m + 1) // 2
        x = total_candies_put - k
        if x >= 0 and n==m+x:
            return x

n, k = map(int, input().strip().split())

result = find_candies_eaten(n, k)
print(result)