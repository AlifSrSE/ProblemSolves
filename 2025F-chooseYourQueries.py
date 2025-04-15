# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve():
    n, q = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    edges = [None] * (q + 1)
    for i in range(1, q + 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append((v, i))
        adj[v].append((u, i))
        edges[i] = (u, v)

    chose = [0] * (q + 1)
    visited = [False] * (n + 1)
    cnt = [0] * (n + 1)

    def dfs(d, fa, ID):
        visited[d] = True
        lst = 0
        for neighbor, edge_id in adj[d]:
            if edge_id == ID:
                continue
            if not visited[neighbor]:
                dfs(neighbor, d, edge_id)
            if not chose[edge_id]:
                if lst == 0:
                    lst = edge_id
                else:
                    chose[lst] = d
                    chose[edge_id] = d
                    cnt[d] += 1
                    lst = 0
        if lst != 0 and ID != 0:
            chose[ID] = d
            chose[lst] = d
            cnt[d] += 1

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, 0, 0)

    results = []
    for i in range(1, q + 1):
        if chose[i] == 0:
            results.append("x+")
            continue
        u, v = edges[i]
        if chose[i] == u:
            results.append("x")
        else:
            results.append("y")
        cnt[chose[i]] -= 1
        if cnt[chose[i]] >= 0:
            results[-1] += "+"
        else:
            results[-1] += "-"
        results.append("\n")

    sys.stdout.write("".join(results))

if __name__ == "__main__":
    solve()