# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2051/problem/B

def solve():
    n, a, b, c = map(int, input().split())
    ans = 3 * (n // (a + b + c))
    n %= (a + b + c)
    if n > 0:
        ans += 1
        n -= a
    if n > 0:
        ans += 1
        n -= b
    if n > 0:
        ans += 1
        n -= c
    print(ans)

t = int(input())
for _ in range(t):
    solve()