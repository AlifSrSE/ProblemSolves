# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2060/problem/D
 
import sys
 
def solve():
    n = int(sys.stdin.readline())
    ara = list(map(int, sys.stdin.readline().split()))
 
    if all(ara[i] <= ara[i + 1] for i in range(n - 1)):
        sys.stdout.write("YES\n")
        return
 
    for _ in range(n - 1):
        for i in range(n - 1):
            x, y = ara[i], ara[i + 1]
            min_val = min(x, y)
            ara[i] -= min_val
            ara[i + 1] -= min_val
 
        if all(ara[i] <= ara[i + 1] for i in range(n - 1)):
            sys.stdout.write("YES\n")
            return
 
    sys.stdout.write("NO\n")
 
t = int(sys.stdin.readline())
for _ in range(t):
    solve()