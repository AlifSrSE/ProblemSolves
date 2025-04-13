# Author: AlifSrSe
# date: 2025-03-27
# https://codeforces.com/problemset/problem/2091/G
 
def solve():
    s, k = map(int, input().split())

    if s % k == 0:
        print(k)
        return

    if s > k * k:
        print(max(1, k - 2))
        return

    f = [False] * (s + 1)
    f[0] = True
    for i in range(k, 0, -1):
        if (k - i) % 2 == 0:
            for x in range(s, -1, -1):
                f[x] = x >= i and f[x - i]
            for x in range(i, s + 1):
                f[x] = f[x] or f[x - i]
        else:
            for x in range(0, s + 1):
                f[x] = x + i <= s and f[x + i]
            for x in range(s - i, -1, -1):
                f[x] = f[x] or f[x + i]
        if f[s]:
            print(i)
            return

    print(1)

t = int(input())
for _ in range(t):
    solve()