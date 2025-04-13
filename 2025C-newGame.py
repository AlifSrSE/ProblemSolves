# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    st = set(a[1:])
    a.sort()
    l = 1
    r = 1
    ans = 0
    while l <= n:
        r = max(l, r)
        while r < n and a[r + 1] - a[r] <= 1 and a[r + 1] - a[l] < k:
            r += 1
        ans = max(ans, r - l + 1)
        l += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()