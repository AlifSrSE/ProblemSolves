# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/263/C

def dfs(start_node, graph, path, visited):
    stack = [start_node]
    visited[start_node] = True
    while stack:
        node = stack.pop()
        path.append(node)
        adj = graph[node]
        for nn in adj:
            if not visited[nn]:
                visited[nn] = True
                stack.append(nn)
                break

def solve():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    path = []
    visited = [False] * (n + 1)
    dfs(1, graph, path, visited)

    last = path[-1]
    neighbors = set(graph[last])

    start = 0
    while path[start] not in neighbors:
        start += 1
    print(len(path) - start)
    print(*path[start:])

solve()