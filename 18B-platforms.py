# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/18/B

def solve():
    n, d, m, l = map(int, input().split())

    ans = 0
    for a in range(n):
        b = m * a + l + d
        ans = b - b % d
        if b - b % d < m * (a + 1):
            break

    print(ans)

solve()