# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2040/A

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = -1
    for i in range(n):
        cnt = 0
        for r in range(n):
            if i == r:
                continue
            d = abs(a[i] - a[r])
            if d % k != 0:
                cnt += 1
        if cnt == n - 1:
            ans = i
            break
    
    if ans == -1:
        print("NO")
    else:
        print("YES")
        print(ans + 1)

t = int(input())
for _ in range(t):
    solve()