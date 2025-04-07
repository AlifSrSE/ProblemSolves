# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

MOD = 1000000007

def count_magic_numbers(a, k):
    n = len(a)
    
    dp = {}
    
    def solve_single(pos, rem, used):
        if pos == n:
            return 1 if rem == 0 and used else 0
            
        state = (pos, rem, used)
        if state in dp:
            return dp[state]
        
        ways = solve_single(pos + 1, rem, used)
        
        digit = int(a[pos])
        new_rem = (rem * 10 + digit) % 5
        ways = (ways + solve_single(pos + 1, new_rem, True)) % MOD
        
        dp[state] = ways
        return ways
    
    single_result = solve_single(0, 0, False)
    
    if k == 1:
        return single_result
    
    dp.clear()
    one_copy_zero = solve_single(0, 0, False)
    
    total = 0
    for i in range(n):
        dp.clear()
        prefix_ways = solve_single(0, 0, False)
        
        remaining_len = n - i
        total_ways = prefix_ways
        
        if remaining_len > 0:
            power = k - 1
            if one_copy_zero != 0:
                total_ways = (total_ways * (pow(2, power * n, MOD) - 1)) % MOD
                total_ways = (total_ways * pow(one_copy_zero, MOD-2, MOD)) % MOD
        
        total = (total + total_ways) % MOD
    
    return total

a = input().strip()
k = int(input())

print(count_magic_numbers(a, k))