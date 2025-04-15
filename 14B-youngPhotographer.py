# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/14/B

def solve():
    n, x0 = map(int, input().split())
    m = 0
    M = 1001

    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        if b < M:
            M = b
        if a > m:
            m = a

    if m > M:
        print("-1")
    else:
        ans = 1001
        if m <= x0 <= M:
            ans = 0
        if x0 < m and ans > m - x0:
            ans = m - x0
        if x0 > M and ans > x0 - M:
            ans = x0 - M
        print(ans)

solve()