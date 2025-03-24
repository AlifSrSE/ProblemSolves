# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2009/A

def solve():
    a, b = map(int, input().split())
    print(b - a)

t = int(input())
for _ in range(t):
    solve()