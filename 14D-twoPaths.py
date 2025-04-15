# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Problem: https://codeforces.com/problemset/problem/14/D

def dfs(node, from_node, graph, length, dist, furthest):
    if length > dist[0]:
        dist[0] = length
        furthest[0] = node
    for u in range(len(graph[node])):
        if not graph[node][u]:
            continue
        if u == from_node:
            continue
        dfs(u, node, graph, length + 1, dist, furthest)
    return

def get_diameter(graph, start):
    root = start
    furthest = [start]
    length = 0
    max_dist = [0]
    dfs(root, -1, graph, length, max_dist, furthest)

    root = furthest[0]
    length = 0
    max_dist = [0]
    dfs(root, -1, graph, length, max_dist, furthest)

    return max_dist[0]

def solve():
    n = int(input())
    graph = [[False] * n for _ in range(n)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        graph[x][y] = graph[y][x] = True

    profit = 0
    for p in range(n):
        for q in range(p + 1, n):
            if not graph[p][q]:
                continue
            graph[p][q] = graph[q][p] = False
            len_a = get_diameter(graph, p)
            len_b = get_diameter(graph, q)
            graph[p][q] = graph[q][p] = True
            prod = len_a * len_b
            profit = max(profit, prod)

    print(profit)

solve()