# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/C
 
def solve():
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        ans = []
        for i in range(n):
            ans.append((i * 2) % n + 1)
        print(*ans)

t = int(input())
for _ in range(t):
    solve()