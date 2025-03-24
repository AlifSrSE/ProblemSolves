# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2032/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = a.count(1)
    print(cnt % 2, min(cnt, n - (cnt - n) if cnt > n else cnt))

t = int(input())
for _ in range(t):
    solve()