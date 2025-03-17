# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/C1
 
import sys
 
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())
 
    res = True
    a[0] = min(a[0], b - a[0])
    for p in range(1, n):
        if not res:
            break
        if a[p - 1] <= a[p] and a[p - 1] <= b - a[p]:
            a[p] = min(a[p], b - a[p])
        elif a[p - 1] <= a[p]:
            continue
        elif a[p - 1] <= b - a[p]:
            a[p] = b - a[p]
        else:
            res = False
 
    print("YES" if res else "NO")