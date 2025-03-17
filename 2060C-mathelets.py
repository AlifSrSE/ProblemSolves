# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2060/problem/C

def solve():
    n, k = map(int, input().split())
    ara = list(map(int, input().split()))
    ara.sort()
    
    sum_pairs = 0
    l, r = 0, n - 1
    
    while l < r:
        if ara[l] + ara[r] == k:
            sum_pairs += 1
            l += 1
            r -= 1
        elif ara[l] + ara[r] < k:
            l += 1
        else:
            r -= 1
    
    print(sum_pairs)

t = int(input())
for _ in range(t):
    solve()