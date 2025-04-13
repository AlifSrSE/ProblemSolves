# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import heapq

def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    pref = [0] * (n + 1)
    dist = [float('inf')] * (n + 1)

    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + a[i]

    pq = [(0, 1)]
    dist[1] = 0

    while pq:
        d, u = heapq.heappop(pq)
        if dist[u] < d:
            continue
        dist[u] = d

        mx = b[u]
        if dist[mx] > dist[u] + a[u]:
            heapq.heappush(pq, (dist[u] + a[u], mx))

        if u >= 2 and dist[u - 1] > dist[u]:
            heapq.heappush(pq, (dist[u], u - 1))

    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, pref[i] - dist[i])
    print(ans)

t = int(input())
for _ in range(t):
    solve()