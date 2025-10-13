# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
sys.setrecursionlimit(300000)

def alif():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        graph = [[] for _ in range(n+1)]
        
        for __ in range(n-1):
            u = int(data[idx]); v = int(data[idx+1])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [0] * (n+1)
        size = [0] * (n+1)
        
        def dfs(u, p):
            parent[u] = p
            size[u] = 1
            for v in graph[u]:
                if v != p:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(1, 0)
        
        centroid = 1
        for u in range(1, n+1):
            max_comp = n - size[u]
            for v in graph[u]:
                if v != parent[u]:
                    max_comp = max(max_comp, size[v])
            if max_comp <= n//2:
                centroid = u
                break
        
        parent2 = [0] * (n+1)
        size2 = [0] * (n+1)
        
        def dfs2(u, p):
            parent2[u] = p
            size2[u] = 1
            for v in graph[u]:
                if v != p:
                    dfs2(v, u)
                    size2[u] += size2[v]
        
        dfs2(centroid, 0)
        
        max_size = 0
        heavy_child = 0
        for v in graph[centroid]:
            if size2[v] > max_size:
                max_size = size2[v]
                heavy_child = v
        
        leaf = heavy_child
        while graph[leaf]:
            next_node = -1
            for v in graph[leaf]:
                if v != parent2[leaf]:
                    next_node = v
                    break
            if next_node == -1:
                break
            leaf = next_node
        
        results.append(f"{leaf} {parent2[leaf]}")
        results.append(f"{leaf} {centroid}")
    
    print("\n".join(results))

if __name__ == "__main__":
    alif()