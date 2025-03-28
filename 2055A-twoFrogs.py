# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2055/problem/A

def solve(n, a, b):
    return abs(a - b) % 2 == 0

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print("YES" if solve(n, a, b) else "NO")