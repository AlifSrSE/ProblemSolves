# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
import heapq

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    sx, sy, fx, fy = map(int, input().split())

    pts = []
    for i in range(m):
        x, y = map(int, input().split())
        pts.append((x, y, i))

    START = m
    FINISH = m + 1
    N = m + 2

    graph = [[] for _ in range(N)]
    pts_sorted_x = sorted(pts)

    for i in range(m - 1):
        _, _, id1 = pts_sorted_x[i]
        x2, y2, id2 = pts_sorted_x[i+1]
        x1 = pts_sorted_x[i][0]
        w = x2 - x1
        graph[id1].append((id2, w))
        graph[id2].append((id1, w))
    pts_sorted_y = sorted(pts, key=lambda t: t[1])

    for i in range(m - 1):
        x1, y1, id1 = pts_sorted_y[i]
        x2, y2, id2 = pts_sorted_y[i+1]
        w = y2 - y1
        graph[id1].append((id2, w))
        graph[id2].append((id1, w))

    for x, y, idx in pts:
        w = min(abs(sx - x), abs(sy - y))
        graph[START].append((idx, w))

    for x, y, idx in pts:
        w = abs(fx - x) + abs(fy - y)
        graph[idx].append((FINISH, w))

    graph[START].append((FINISH, abs(fx - sx) + abs(fy - sy)))

    dist = [10**30] * N
    dist[START] = 0
    pq = [(0, START)]

    while pq:
        d, v = heapq.heappop(pq)
        if d != dist[v]:
            continue
        if v == FINISH:
            break
        for to, w in graph[v]:
            nd = d + w
            if nd < dist[to]:
                dist[to] = nd
                heapq.heappush(pq, (nd, to))
    print(dist[FINISH])

if __name__ == "__main__":
    main()
