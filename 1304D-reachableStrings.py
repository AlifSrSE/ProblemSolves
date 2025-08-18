import sys
sys.setrecursionlimit(200000)

def alif():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    MAX_LOG_N = 18
    depth = [-1] * (n + 1)
    parent = [[0] * (MAX_LOG_N + 1) for _ in range(n + 1)]

    def dfs(u, p, d):
        depth[u] = d
        parent[u][0] = p
        for v in graph[u]:
            if v != p:
                dfs(v, u, d + 1)
    dfs(1, 0, 0)

    for j in range(1, MAX_LOG_N + 1):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j-1]][j-1]

    def get_ancestor(u, k):
        for j in range(MAX_LOG_N, -1, -1):
            if k & (1 << j):
                u = parent[u][j]
        return u

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        u = get_ancestor(u, depth[u] - depth[v])

        if u == v:
            return u

        for j in range(MAX_LOG_N, -1, -1):
            if parent[u][j] != parent[v][j]:
                u = parent[u][j]
                v = parent[v][j]
        
        return parent[u][0]

    def dist(u, v):
        lca_node = lca(u, v)
        return depth[u] + depth[v] - 2 * depth[lca_node]

    q = int(sys.stdin.readline())
    for _ in range(q):
        x, y, a, b, k = map(int, sys.stdin.readline().split())
        dist_ab_tree = dist(a, b)
        can_reach_direct = (k >= dist_ab_tree) and ((k - dist_ab_tree) % 2 == 0)

        dist_ax = dist(a, x)
        dist_by = dist(b, y)
        path2_len = dist_ax + 1 + dist_by
        can_reach_via_xy = (k >= path2_len) and ((k - path2_len) % 2 == 0)

        dist_ay = dist(a, y)
        dist_bx = dist(b, x)
        path3_len = dist_ay + 1 + dist_bx
        
        can_reach_via_yx = (k >= path3_len) and ((k - path3_len) % 2 == 0)
        if can_reach_direct or can_reach_via_xy or can_reach_via_yx:
            print("YES")
        else:
            print("NO")

alif()