# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/C2
 
import sys
from bisect import bisect_left
 
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    b.sort()
 
    res = True
    a[0] = min(a[0], b[0] - a[0])
    for p in range(1, n):
        if not res:
            break
            
        fb_idx = bisect_left(b, a[p - 1] + a[p])
        if fb_idx == len(b):
            if a[p - 1] > a[p]:
                res = False
                break
            continue
 
        fb = b[fb_idx]
        if a[p - 1] <= a[p] and a[p - 1] <= fb - a[p]:
            a[p] = min(a[p], fb - a[p])
        elif a[p - 1] <= a[p]:
            continue
        elif a[p - 1] <= fb - a[p]:
            a[p] = fb - a[p]
        else:
            res = False
 
    print("YES" if res else "NO")