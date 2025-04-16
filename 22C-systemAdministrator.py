# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/22/C

def solve():
    n, m, v = map(int, input().split())
    if m < n - 1 or m > n * (n - 1) // 2:
        print("-1")
        return
    if m > 1 + (n - 1) * (n - 2) // 2:
        print("-1")
        return

    w = 2 if v == 1 else 1
    for p in range(1, n + 1):
        if v == p:
            continue
        print(v, p)

    m -= (n - 1)
    for p in range(1, n + 1):
        if m <= 0:
            break
        if p == v or p == w:
            continue
        for q in range(p + 1, n + 1):
            if q == v or q == w:
                continue
            print(p, q)
            m -= 1
            if m <= 0:
                break

solve()