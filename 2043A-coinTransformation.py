# Author : AlifSrSE
# Date : 2025-03-25
# Problem link : https://codeforces.com/contest/2043/problem/A

def solve():
    n = int(input())
    
    def calculate_max_coins(x):
        if x <= 3:
            return 1
        return 2 * calculate_max_coins(x // 4)
    
    print(calculate_max_coins(n))

t = int(input())
for _ in range(t):
    solve()