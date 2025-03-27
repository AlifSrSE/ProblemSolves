# Author : AlifSrSE
# Date : 2025-03-27
# Problem link : https://codeforces.com/contest/2046/problem/A

def solve():
    n = int(input())
    a = []
    for _ in range(2):
        a.append(list(map(int, input().split())))

    max_sums = sum(max(a[0][c], a[1][c]) for c in range(n))
    max_mins = max(min(a[0][c], a[1][c]) for c in range(n))

    print(max_sums + max_mins)

t = int(input())
for _ in range(t):
    solve()