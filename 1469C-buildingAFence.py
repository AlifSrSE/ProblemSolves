# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1469/problem/C

def solve():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    l = a[1]
    r = a[1]

    for i in range(2, n + 1):
        tl = a[i]
        tr = a[i] + k - 1
        l = max(tl, l - k + 1)
        r = min(tr, r + k - 1)
        if l > a[i] + k - 1:
            print("NO")
            return
        if l > r:
            print("NO")
            return

    if l == a[n]:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()