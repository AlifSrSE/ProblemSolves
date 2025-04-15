# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/20/C

import heapq

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))

    source, target = 1, n
    q = [(0, source)]
    dist = [-1] * (n + 1)
    from_node = [-1] * (n + 1)
    from_node[0] = 0
    from_node[1] = 1
    visited = [False] * (n + 1)

    while q:
        distance, vertex = heapq.heappop(q)
        if visited[vertex]:
            continue
        visited[vertex] = True
        for u, w in g[vertex]:
            if visited[u]:
                continue
            if dist[u] < 0 or dist[u] > distance + w:
                dist[u] = distance + w
                heapq.heappush(q, (dist[u], u))
                from_node[u] = vertex

    if dist[n] < 0:
        print("-1")
    else:
        st = [n]
        while st[-1] != from_node[st[-1]]:
            st.append(from_node[st[-1]])
        print(*reversed(st))

solve()