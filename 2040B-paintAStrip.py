# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2040/B

def solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n <= 3:
        print(2)
    else:
        cnt = 2
        d = 4
        while d * 2 + 2 <= n:
            cnt += 1
            d = d * 2 + 2
        if d < n:
            cnt += 1
        print(cnt)

t = int(input())
for _ in range(t):
    solve()