# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2019/B

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    m = {}
    for i in range(n):
        d = (i + 1) * (n - i) - 1
        m[d] = m.get(d, 0) + 1
        if i + 1 < n:
            if a[i + 1] - a[i] > 1:
                d = (i + 1) * (n - i - 1)
                m[d] = m.get(d, 0) + (a[i + 1] - a[i] - 1)
    
    queries = list(map(int, input().split()))
    result = []
    for k in queries:
        result.append(m.get(k, 0))
    print(*result)

t = int(input())
for _ in range(t):
    solve()