# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2037/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = {}
    for i in a:
        m[i] = m.get(i, 0) + 1
    ans = 0
    for v in m.values():
        ans += v // 2
    print(ans)

t = int(input())
for _ in range(t):
    solve()