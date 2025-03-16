# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/A

def solve():
    a, b = map(int, input().split())
    if (a % 2 != 0) or (b % 2 != 0 and a < 2):
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()