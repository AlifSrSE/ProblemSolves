# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
from collections import deque

def bfs(n, adj, color):
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([(1, -1)])
    
    while q:
        u, prev_t = q.popleft()
        for v, t in adj[u]:
            if t == color[u] and (prev_t == -1 or prev_t == color[u]):
                if dist[v] == -1 or dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    q.append((v, t))
    
    return dist[n]

def alif():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, t = map(int, input().split())
        adj[u].append((v, t))
    
    max_dist = -1
    best_color = [0] * (n + 1)
    
    for mask in range(1 << n):
        color = [0] * (n + 1)
        for i in range(n):
            color[i + 1] = (mask >> i) & 1
        dist = bfs(n, adj, color)
        if dist == -1 or dist > max_dist:
            max_dist = dist
            best_color = color[:]
    
    print(max_dist)
    print(''.join(map(str, best_color[1:])), flush=True)

alif()