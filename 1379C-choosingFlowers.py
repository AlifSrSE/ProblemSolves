# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from bisect import bisect_left

def alif():
    n, m = map(int, sys.stdin.readline().split())
    flowers = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        flowers.append((a, b))

    flowers.sort(key=lambda x: x[0], reverse=True)
    a_values = [f[0] for f in flowers]
    prefix_sum_a = [0] * (m + 1)
    for i in range(m):
        prefix_sum_a[i+1] = prefix_sum_a[i] + a_values[i]

    max_happiness = 0
    for i in range(m):
        a_i, b_i = flowers[i]
        num_distinct = min(n, m)
        current_a_sum = prefix_sum_a[i+1]
        remaining_slots = n - (i+1)
        
        if remaining_slots >= 0:
            current_happiness = current_a_sum + remaining_slots * b_i
            max_happiness = max(max_happiness, current_happiness)
            
        k = m - bisect_left(a_values, b_i, key=lambda x: -x)
        num_to_take = min(n - 1, k)
        sum_a_bonus = prefix_sum_a[num_to_take]
        if a_i >= b_i:
            
            idx = bisect_left(a_values, a_i, key=lambda x: -x)
            if idx < num_to_take:
                sum_a_bonus -= a_i
                
        remaining_slots = n - 1 - num_to_take
        current_happiness = a_i + sum_a_bonus + remaining_slots * b_i
        max_happiness = max(max_happiness, current_happiness)

    print(max_happiness)

t = int(sys.stdin.readline())
for _ in range(t):
    alif()