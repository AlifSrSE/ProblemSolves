# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2037/B

def solve():
    k = int(input())
    a = list(map(int, input().split()))
    m = {}
    for i in a:
        m[i] = m.get(i, 0) + 1
    v = k - 2
    for i in range(1, int(v**0.5) + 1):
        if v % i == 0:
            vv = v // i
            if i != vv:
                if m.get(i, 0) and m.get(vv, 0):
                    print(i, vv)
                    return
            else:
                if m.get(i, 0) >= 2:
                    print(i, vv)
                    return

t = int(input())
for _ in range(t):
    solve()