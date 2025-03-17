# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1994/problem/C

def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    index = 0
    t = data[index]
    index += 1
    for _ in range(t):
        n = data[index]
        x = data[index + 1]
        index += 2
        a = data[index:index + n]
        index += n
        print(solve(a, x))

def solve(a, x):
    n = len(a)
    
    next_indices = [0] * n
    sum_val = 0
    end_index = -1
    for i in range(n):
        while end_index != n - 1 and sum_val <= x:
            end_index += 1
            sum_val += a[end_index]
        
        next_indices[i] = -1 if (end_index == n - 1 and sum_val <= x) else (end_index + 1)
        
        sum_val -= a[i]
    
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if next_indices[i] != -1:
            dp[i] = 1 + (0 if next_indices[i] == n else dp[next_indices[i]])
    
    total_subarrays = n * (n + 1) // 2
    sum_dp = sum(dp)
    return total_subarrays - sum_dp

if __name__ == "__main__":
    main()