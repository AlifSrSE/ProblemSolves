# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1254/problem/B1

import math

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    total_chocolates = sum(a)

    if total_chocolates == 1:
        print(-1)
        return

    min_total_seconds = float('inf')
    temp_s = total_chocolates
    prime_factors = set()
    
    if temp_s % 2 == 0:
        prime_factors.add(2)
        while temp_s % 2 == 0:
            temp_s //= 2

    for i in range(3, int(math.sqrt(temp_s)) + 1, 2):
        if temp_s % i == 0:
            prime_factors.add(i)
            while temp_s % i == 0:
                temp_s //= i

    if temp_s > 1:
        prime_factors.add(temp_s)

    for k in prime_factors:
        current_prefix_sum = 0
        current_cost_for_k = 0
        
        for x in a:
            current_prefix_sum += x
            remainder = current_prefix_sum % k
            current_cost_for_k += min(remainder, k - remainder)
        
        min_total_seconds = min(min_total_seconds, current_cost_for_k)

    print(min_total_seconds)

alif()