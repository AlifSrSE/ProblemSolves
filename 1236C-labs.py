# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    v = list(range(1, n * n + 1))
    a = [[0] * n for _ in range(n)]
    m = 0
    k = 0
    z = 1

    for i in range(1, n * n + 1, n):
        if z % 2:
            for j in range(n - 1, -1, -1):
                a[j][k] = v[m]
                m += 1
            k += 1
        else:
            for j in range(n):
                a[j][k] = v[m]
                m += 1
            k += 1
        z += 1

    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()

solve()