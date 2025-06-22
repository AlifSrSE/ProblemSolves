# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1230/problem/C

def alif():
    n, m = map(int, input().split())
    if n <= 6:
        print(m)
        return
    g = [[0] * n for _ in range(n)]

    for _ in range(m):
        x, y = map(int, input().split())
        g[x - 1][y - 1] = 1
        g[y - 1][x - 1] = 1
    mn = float('inf')

    for a in range(n):
        for b in range(n):
            x = 0
            for c in range(n):
                if g[c][a] and g[c][b]:
                    x += 1
            mn = min(mn, x)
    print(m - mn)

if __name__ == "__main__":
    alif()