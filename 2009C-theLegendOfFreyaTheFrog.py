# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2009/C

def solve():
    x, y, k = map(int, input().split())
    if x > y:
        ans = (x + k - 1) // k
        ans += max((y + k - 1) // k, ans - 1)
    else:
        ans = (y + k - 1) // k
        ans += max(ans, (x + k - 1) // k)
    print(ans)

t = int(input())
for _ in range(t):
    solve()