# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def solve():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    gcd = math.gcd(a[0][1], a[0][2])
    for i in range(3, n):
        gcd = math.gcd(gcd, a[0][i])

    k = 0
    for i in range(1, int(math.sqrt(gcd)) + 1):
        if gcd % i == 0:
            a0 = i
            a1 = a[0][1] // a0
            a2 = a[0][2] // a0
            if a1 * a2 == a[1][2]:
                k = a0
                break

            a0 = gcd // i
            a1 = a[0][1] // a0
            a2 = a[0][2] // a0
            if a1 * a2 == a[1][2]:
                k = a0
                break

    ar = [0] * n
    ar[0] = k
    for i in range(1, n):
        ar[i] = a[0][i] // k

    print(*ar)

solve()