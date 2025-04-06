# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [0] * n
    suf = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        c[i] = a[i] // b[i]
        suf[i] = c[i] + suf[i + 1]

    d = [0] * n
    for i in range(n):
        d[i] = min(c[i], max(0, k - suf[i + 1]))
        k -= d[i]

    if k > 0:
        d = [0] * n

    print(*d)

if __name__ == "__main__":
    solve()