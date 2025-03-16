# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/G
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    total_sum = 0
 
    def calculate_f(b):
        if not b:
            return 0
        if len(b) == 1:
            return 1 if b[0] > 0 else 0
 
        max_val = max(b)
        if max_val == 0:
            return 0
 
        operations = 1
        current_b = list(b)
        while max(current_b) > 0:
            new_b = []
            for val in current_b:
                new_b.append(max(0, val - 1))
            current_b = new_b
            if max(current_b) > 0:
                operations += 1
        return operations
 
    for l in range(n):
        for r in range(l, n):
            sub_array = a[l:r + 1]
            total_sum = (total_sum + calculate_f(sub_array)) % mod
 
    print(total_sum)
 
t = int(input())
for _ in range(t):
    solve()