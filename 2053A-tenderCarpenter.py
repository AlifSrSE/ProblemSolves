# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2053/problem/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n - 1):
        if 2 * min(a[i], a[i + 1]) > max(a[i], a[i + 1]):
            print("YES")
            return
    print("NO")

t = int(input())
for _ in range(t):
    solve()