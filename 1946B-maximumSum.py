# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1946/B
 
MODULUS = 1_000_000_007

def solve(a, k):
    max_sum = 0
    current_sum = 0
    for ai in a:
        current_sum = max(0, current_sum + ai)
        max_sum = max(max_sum, current_sum)

    result = 0
    current_sum = int(max_sum % MODULUS)
    for _ in range(k):
        result = (result + current_sum) % MODULUS
        current_sum = (current_sum + current_sum) % MODULUS
    for ai in a:
        result = (result + ai) % MODULUS
    return result

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(a, k))