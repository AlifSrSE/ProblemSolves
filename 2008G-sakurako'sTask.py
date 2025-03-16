# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/G

import math

def solve():
    num_tests = int(input())
    for _ in range(num_tests):
        size, limit = map(int, input().split())
        values = list(map(int, input().split()))
        common_divisor = 0
        maximum_value = 0
        for val in values:
            common_divisor = math.gcd(common_divisor, val)
            maximum_value = max(maximum_value, val)
        if common_divisor == 0:
            print(limit)
            continue
        values.sort()
        cumulative_sum = -common_divisor
        if size != 1:
            for index in range(size):
                cumulative_sum += common_divisor
                values[index] = cumulative_sum
        values.append(10**16)
        last_position = -1
        for index in range(size + 1):
            if limit <= values[index] - last_position - 1:
                break
            limit -= max(values[index] - last_position - 1, 0)
            last_position = values[index]
        print(last_position + limit)

solve()