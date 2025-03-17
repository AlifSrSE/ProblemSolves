# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2051/problem/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        if a[i] > b[i + 1]:
            ans += (a[i] - b[i + 1])
    ans += a[n - 1]
    print(ans)

t = int(input())
for _ in range(t):
    solve()
