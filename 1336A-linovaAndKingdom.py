# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def dfs(node, parent, graph, depth, potentials):
    size = 1
    for neighbor in graph[node]:
        if neighbor != parent:
            size += dfs(neighbor, node, graph, depth + 1, potentials)
    
    potentials.append(size - depth)
    return size

def alif():
    sys.setrecursionlimit(200000)
    try:
        n, k = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            x, y = map(int, sys.stdin.readline().split())
            graph[x].append(y)
            graph[y].append(x)
        
        potentials = []
        dfs(1, 0, graph, 1, potentials)
        
        potentials.sort(reverse=True)
        
        total_happiness = sum(potentials[:k])
        
        sys.stdout.write(str(total_happiness) + '\n')

    except (IOError, ValueError):
        pass

if __name__ == "__main__":
    alif()