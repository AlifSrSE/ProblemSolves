# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2037/D

import heapq

def solve(l, r, x, v, L):
    result = 0
    power = 1
    ups = []
    up_index = 0
    for i in range(len(l)):
        while up_index != len(x) and x[up_index] < l[i]:
            heapq.heappush(ups, -v[up_index])
            up_index += 1

        while power < r[i] - l[i] + 2:
            if not ups:
                return -1

            power += -heapq.heappop(ups)
            result += 1

    return result

t = int(input())
for _ in range(t):
    n, m, L = map(int, input().split())
    l = []
    r = []
    for _ in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    x = []
    v = []
    for _ in range(m):
        xi, vi = map(int, input().split())
        x.append(xi)
        v.append(vi)

    print(solve(l, r, x, v, L))