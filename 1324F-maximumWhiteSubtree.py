# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

from collections import defaultdict

def alif(n, colors, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    values = [1 if c == 1 else -1 for c in colors]
    dp = [0] * n
    subtree_sum = [0] * n
    visited = [False] * n
    
    def dfs_subtree(node, parent):
        subtree_sum[node] = values[node]
        dp[node] = values[node]
        
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs_subtree(neighbor, node)
                subtree_sum[node] += subtree_sum[neighbor]
                dp[node] = max(dp[node], subtree_sum[node], subtree_sum[neighbor])
    dfs_subtree(0, -1)
    
    def reroot(node, parent):
        for neighbor in graph[node]:
            if neighbor != parent:
                node_sum = subtree_sum[node]
                neighbor_sum = subtree_sum[neighbor]
                
                subtree_sum[node] -= subtree_sum[neighbor]
                subtree_sum[neighbor] += subtree_sum[node]
                dp[neighbor] = max(dp[neighbor], subtree_sum[neighbor], subtree_sum[node])
                reroot(neighbor, node)
                
                subtree_sum[node] = node_sum
                subtree_sum[neighbor] = neighbor_sum
    reroot(0, -1)
    return dp

n = int(input())
colors = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n-1)]

result = alif(n, colors, edges)
print(*result)