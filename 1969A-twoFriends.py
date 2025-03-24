# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/1969/A
 
def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ans = float('inf')
    for i in range(1, n + 1):
        if a[i] < 0:
            continue
        cnt = 0
        now = a[i]
        p = i
        while now > 0:
            cnt += 1
            a[p] = -1
            p = now
            now = a[now]
        ans = min(ans, cnt)
    print(min(ans, 3))
 
t = int(input())
for _ in range(t):
    solve()