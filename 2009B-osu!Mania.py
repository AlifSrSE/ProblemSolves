# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2009/B

def solve():
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        for k, char in enumerate(s):
            if char == '#':
                a.append(k + 1)
    a.reverse()
    print(*a)

t = int(input())
for _ in range(t):
    solve()