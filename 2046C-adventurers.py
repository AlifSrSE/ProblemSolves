# Author : AlifSrSE
# Date : 2025-03-27
# Problem link : https://codeforces.com/contest/2046/problem/C

def solve():
    n = int(input())
    cities = []
    for _ in range(n):
        cities.append(list(map(int, input().split())))

    best_k = 0
    best_x = 0
    best_y = 0

    for x0, y0 in cities:
        k = float('inf')
        counts = [0, 0, 0, 0]
        for xi, yi in cities:
            if x0 <= xi and y0 <= yi:
                counts[0] += 1
            elif x0 > xi and y0 <= yi:
                counts[1] += 1
            elif x0 <= xi and y0 > yi:
                counts[2] += 1
            else:
                counts[3] += 1
        k = min(counts)
        if k > best_k:
            best_k = k
            best_x = x0
            best_y = y0

    print(best_k)
    print(best_x, best_y)

t = int(input())
for _ in range(t):
    solve()