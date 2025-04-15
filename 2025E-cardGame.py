# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    mod = 998244353
    f = [[0] * (m + 1) for _ in range(m + 1)]
    g = [[0] * (m + 1) for _ in range(n)]

    f[0][0] = 1
    for i in range(m):
        for j in range(i + 1):
            f[i + 1][j + 1] = (f[i + 1][j + 1] + f[i][j]) % mod
            if j > 0:
                f[i + 1][j - 1] = (f[i + 1][j - 1] + f[i][j]) % mod

    g[0][0] = 1
    for i in range(n - 1):
        for j in range(m + 1):
            for k in range(m - j + 1):
                g[i + 1][j + k] = (g[i + 1][j + k] + g[i][j] * f[m][k]) % mod

    ans = 0
    for i in range(m + 1):
        ans = (ans + f[m][i] * g[n - 1][i]) % mod
    print(ans)

if __name__ == "__main__":
    T = 1
    for _ in range(T):
        solve()