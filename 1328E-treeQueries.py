# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

from collections import defaultdict

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    return graph

def find_path(graph, start, end, parent):
    path = []
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, curr_path = stack.pop()
        if node == end:
            return curr_path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    stack.append((neighbor, curr_path + [neighbor]))
    return []

def can_satisfy_query(graph, n, vertices):
    if not vertices:
        return True
    vertices = [v-1 for v in vertices]
    max_depth_vertex = max(vertices, key=lambda x: depth[x])
    path = find_path(graph, 0, max_depth_vertex, parent)
    if not path:
        return False
    path_set = set(path)
    for v in vertices:
        if v in path_set:
            continue
        has_neighbor = False
        for neighbor in graph[v]:
            if neighbor in path_set:
                has_neighbor = True
                break
        if not has_neighbor:
            return False
    return True

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(n-1)]
graph = build_graph(n, edges)

depth = [0] * n
parent = [-1] * n
stack = [(0, 0, -1)]
while stack:
    node, d, p = stack.pop()
    depth[node] = d
    parent[node] = p
    for neighbor in graph[node]:
        if neighbor != p:
            stack.append((neighbor, d+1, node))

for _ in range(m):
    query = list(map(int, input().split()))
    k = query[0]
    vertices = query[1:]
    print("YES" if can_satisfy_query(graph, n, vertices) else "NO")