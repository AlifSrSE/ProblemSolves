# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2078/problem/C
 
def solve():
    T = int(input()) 
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
 
        a.sort()  
 
        g = []
        for i in range(n):
            g.append(a[i + n]) 
            g.append(a[i])  
 
        print(g[-2], *g)
solve()