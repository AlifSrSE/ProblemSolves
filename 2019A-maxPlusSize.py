# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2019/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mx1, cnt1, mx2, cnt2 = 0, 0, 0, 0
    for i in range(0, n, 2):
        mx1 = max(mx1, a[i])
        cnt1 += 1
    for i in range(1, n, 2):
        mx2 = max(mx2, a[i])
        cnt2 += 1
    print(max(mx1 + cnt1, mx2 + cnt2))

t = int(input())
for _ in range(t):
    solve()