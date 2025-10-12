# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from collections import deque

input = sys.stdin.read
data = input().split()
idx = 0

t = int(data[idx]); idx += 1
results = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    a = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    da = int(data[idx]); idx += 1
    db = int(data[idx]); idx += 1
    
    graph = [[] for _ in range(n + 1)]
    for __ in range(n - 1):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    
    dist_a = bfs(a)
    if dist_a[b] <= da:
        results.append("Alice")
        continue
    
    farthest_node = 1
    for i in range(2, n + 1):
        if dist_a[i] > dist_a[farthest_node]:
            farthest_node = i
    
    dist_from_farthest = bfs(farthest_node)
    diameter = max(dist_from_farthest[1:])
    
    if 2 * da >= diameter:
        results.append("Alice")
        continue
    
    if db > 2 * da:
        results.append("Bob")
    else:
        results.append("Alice")

print("\n".join(results))