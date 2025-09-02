# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

def highest_power_of_two(x):
    if x == 0:
        return 20
    k = 0
    while x % 2 == 0:
        x //= 2
        k += 1
    return k

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def alif():
    n = int(input())
    edges = []
    for i in range(n):
        a, b = map(int, input().split())
        edges.append((a, b, 2 * i + 1, 2 * i + 2))
    
    lo, hi = 0, 20
    best_b = 0
    best_perm = []
    
    while lo <= hi:
        mid = (lo + hi) // 2
        parent = list(range(2 * n + 1))
        rank = [0] * (2 * n + 1)
        graph = [[] for _ in range(2 * n + 1)]
        used_edges = []
        
        for a, b, u, v in edges:
            if highest_power_of_two(a ^ b) >= mid:
                graph[u].append(v)
                graph[v].append(u)
                used_edges.append((u, v))
        
        for i in range(1, 2 * n + 1, 2):
            u, v = i, i + 1
            graph[u].append(v)
            graph[v].append(u)
            used_edges.append((u, v))
        
        deg = [len(graph[i]) for i in range(2 * n + 1)]
        if max(deg[1:]) > 2:
            hi = mid - 1
            continue
        
        components = 2 * n
        for u, v in used_edges:
            if union(parent, rank, u, v):
                components -= 1
        
        if components == 1 and all(deg[i] == 2 for i in range(1, 2 * n + 1)):
            best_b = mid
            best_perm = []
            visited = [False] * (2 * n + 1)
            stack = [1]
            visited[1] = True
            while stack:
                u = stack[-1]
                best_perm.append(u)
                for v in graph[u]:
                    if not visited[v]:
                        stack.append(v)
                        visited[v] = True
                        break
                else:
                    stack.pop()
            lo = mid + 1
        else:
            hi = mid - 1
    
    print(best_b)
    print(*best_perm)

alif()