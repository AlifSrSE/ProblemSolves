# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/F
 
MOD = 998244353

def can_reach(x1, y1, x2, y2, d):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist <= d * d

def solve():
    n, m, d = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(input().strip())
        grid.append(row)
    
    holds = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                holds[i].append(j)
    
    for i in range(n):
        if not holds[i]:
            print(0)
            return
    
    graph = {}
    nodes = []
    for r in range(1, n+1):
        for col in holds[r-1]:
            node = (r, col)
            nodes.append(node)
            graph[node] = []
    
    for i, (r1, c1) in enumerate(nodes):
        for j, (r2, c2) in enumerate(nodes):
            if r2 > r1:  
                continue
            if can_reach(r1, c1, r2, c2, d):
                graph[(r1, c1)].append((r2, c2))
    
    dp = {}
    for col in holds[n-1]:
        node = (n, col)
        used = [0] * n
        used[n-1] = 1
        state = (1, node, tuple(used))
        dp[state] = 1
    
    for pos in range(1, 2*n):
        dp_next = {}
        for (p, node, used), count in dp.items():
            last_row, last_col = node
            used = list(used)
            for next_node in graph[node]:
                r, c = next_node
                if used[r-1] >= 2:
                    continue
                new_used = used[:]
                new_used[r-1] += 1
                new_state = (pos+1, next_node, tuple(new_used))
                dp_next[new_state] = (dp_next.get(new_state, 0) + count) % MOD
        dp = dp_next
    
    ans = 0
    for (pos, node, used), count in dp.items():
        if pos < n or pos > 2*n:
            continue
        r, c = node
        if r != 1:
            continue
        if any(u == 0 for u in used):
            continue
        ans = (ans + count) % MOD
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()