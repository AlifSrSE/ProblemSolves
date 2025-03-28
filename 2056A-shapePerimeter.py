# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2056/problem/A

def solve(x, y, m):
    return 4 * m + sum(2 * x[i] + 2 * y[i] for i in range(1, len(x)))

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = []
    y = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    print(solve(x, y, m))