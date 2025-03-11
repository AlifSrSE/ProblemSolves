# Author : AlifSrSE
# Date : 2025-03-11
# Problem link : https://codeforces.com/contest/1941/problem/G

from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    adj = defaultdict(set)
    dp = {}
    dis = {}
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].add(c + n)
        adj[c + n].add(a)
        adj[b].add(c + n)
        adj[c + n].add(b)

    s, e = map(int, input().split())

    q = deque([s])
    dis[s] = True
    dp[s] = 0
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dis:
                dis[v] = True
                dp[v] = dp[u] + 1
                q.append(v)
    print(dp.get(e, 0) // 2)

TC = int(input())
for _ in range(TC):
    solve()