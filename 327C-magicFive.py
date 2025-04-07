# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
sys.setrecursionlimit(10**6)

MOD = 1000000007

def count_magic_numbers(a, k):
    n = len(a)
    dp = {}
    
    def solve(pos, rem, used):
        if pos == n:
            return 1 if rem == 0 and used else 0
            
        state = (pos, rem, used)
        if state in dp:
            return dp[state]
        
        ways = solve(pos + 1, rem, used)
        digit = int(a[pos])
        new_rem = (rem * 10 + digit) % 5
        ways = (ways + solve(pos + 1, new_rem, True)) % MOD
        dp[state] = ways
        return ways
    
    dp.clear()
    single_ways = solve(0, 0, False)
    
    if k == 1:
        return single_ways
    
    dp.clear()
    remainders = [0] * 5
    for rem in range(5):
        dp.clear()
        def solve_rem(pos, curr_rem, used):
            if pos == n:
                return 1 if curr_rem == rem and used else 0
            state = (pos, curr_rem, used)
            if state in dp:
                return dp[state]
            ways = solve_rem(pos + 1, curr_rem, used)
            digit = int(a[pos])
            new_rem = (curr_rem * 10 + digit) % 5
            ways = (ways + solve_rem(pos + 1, new_rem, True)) % MOD
            dp[state] = ways
            return ways
        remainders[rem] = solve_rem(0, 0, False)
    
    prev = [0] * 5
    prev[0] = 1
    
    for _ in range(k):
        curr = [0] * 5
        for prev_rem in range(5):
            curr[prev_rem] = (curr[prev_rem] + prev[prev_rem]) % MOD
            for next_rem in range(5):
                if remainders[next_rem] > 0:
                    new_rem = (prev_rem * pow(10, n, 5) + next_rem) % 5
                    curr[new_rem] = (curr[new_rem] + 
                                   (prev[prev_rem] * remainders[next_rem]) % MOD) % MOD
        prev = curr
    
    result = (prev[0] - 1) % MOD
    return result if result >= 0 else result + MOD

a = input().strip()
k = int(input())

print(count_magic_numbers(a, k))