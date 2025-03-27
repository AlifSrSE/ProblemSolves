# Author: AlifSrSe
# date: 2025-03-27
# https://codeforces.com/problemset/problem/2035/A

def solve():
    n, m, r, c = map(int, input().split())
    result = (m - c) + (n - r) * (m * 2 - 1)
    print(result)

t = int(input())
for _ in range(t):
    solve()