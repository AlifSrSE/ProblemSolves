# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2074/problem/A
 
def solve():
    t = int(input())
    for _ in range(t):
        l, r, d, u = map(int, input().split())  
        if l == r and d == u and l == d:
            print("YES")
        else:
            print("NO")
 
solve()