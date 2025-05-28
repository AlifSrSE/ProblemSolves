# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1195/problem/C

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    fa = [0] * n
    fb = [0] * n
    fc = [0] * n

    fa[0] = a[0]
    fb[0] = b[0]
    fc[0] = 0

    for p in range(1, n):
        fa[p] = a[p] + max(fb[p - 1], fc[p - 1])
        fb[p] = b[p] + max(fa[p - 1], fc[p - 1])
        fc[p] = max(fa[p - 1], fb[p - 1])

    ans = max(fa[n - 1], fb[n - 1])
    print(ans)

if __name__ == "__main__":
    alif()