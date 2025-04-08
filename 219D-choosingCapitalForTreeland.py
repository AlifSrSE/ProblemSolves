# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    edges = [[] for _ in range(n + 1)]
    dist = [[0, 0] for _ in range(n + 1)]  
    total_inv = 0

    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        edges[x].append((y, 0))
        edges[y].append((x, 1))

    stack = [(1, 0, False)]
    while stack:
        vertex, parent, processed = stack.pop()
        if not processed:
            stack.append((vertex, parent, True))
            for neighbor, needs_inv in edges[vertex]:
                if neighbor == parent:
                    continue
                if dist[neighbor][0] > 0:
                    continue
                dist[neighbor][0] = 1 + dist[vertex][0]
                dist[neighbor][1] = needs_inv + dist[vertex][1]
                total_inv += needs_inv
                stack.append((neighbor, vertex, False))
        else:
            pass

    capitals = []
    best = n + 1
    for p in range(1, n + 1):
        candidate = total_inv + dist[p][0] - 2 * dist[p][1]
        if candidate == best:
            capitals.append(p)
        elif candidate < best:
            best = candidate
            capitals = [p]

    print(best)
    print(' '.join(map(str, capitals)))

if __name__ == "__main__":
    main()