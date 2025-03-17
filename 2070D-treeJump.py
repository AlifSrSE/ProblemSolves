# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2070/problem/D

MOD = 998244353

def add(x, y):
    x += y
    if x >= MOD:
        x -= MOD
    if x < 0:
        x += MOD
    return x

def solve():
    n = int(input())
    p = [0] * n
    d = [0] * n
    vs = [[] for _ in range(n)]
    
    parent_values = list(map(int, input().split()))
    
    for v in range(1, n):
        p[v] = parent_values[v - 1] - 1 
        d[v] = d[p[v]] + 1
        vs[d[v]].append(v)

    dp = [0] * n
    tot = [0] * n
    dp[0] = tot[0] = 1

    for i in range(1, n):
        for v in vs[i]:
            dp[v] = add(tot[d[v] - 1], 0 if d[v] == 1 else -dp[p[v]])
            tot[d[v]] = add(tot[d[v]], dp[v])

    ans = 0
    for v in range(n):
        ans = add(ans, dp[v])

    print(ans)

t = int(input())
for _ in range(t):
    solve()