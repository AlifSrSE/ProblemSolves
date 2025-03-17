# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2051/problem/D
 
import sys
 
def solve():
    n, x, y = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    sum_a = sum(a)
    y = sum_a - y
    x = sum_a - x
    ans = 0
    for i in range(n):
        l = 0
        r = n
        while l < r:
            mid = (l + r) // 2
            if a[mid] < y - a[i]:
                l = mid + 1
            else:
                r = mid
        left = l
        l = 0
        r = n
        while l < r:
            mid = (l + r) // 2
            if a[mid] <= x - a[i]:
                l = mid + 1
            else:
                r = mid
        right = l
        ans += max(0, right - left)
        if left <= i < right:
            ans -= 1
    ans //= 2
    print(ans)
 
t = int(sys.stdin.readline())
for _ in range(t):
    solve()
