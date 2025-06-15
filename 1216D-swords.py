# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1216/problem/D

import math

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    mx = 0

    if n > 0:
        mx = a[0]
        for p in range(1, n):
            mx = max(mx, a[p])
    differences = []

    for val in a:
        diff = mx - val
        if diff != 0:
            differences.append(diff)
    z = 0

    if len(differences) > 0:
        z = differences[0]
        for i in range(1, len(differences)):
            z = math.gcd(z, differences[i])
    else:
        if len(differences) == 0:
            z = 0
            for p in range(n):
                z = math.gcd(z, mx - a[p])
    y = 0

    if z == 0:
        y = 0

        if n == 1:
            pass
        elif len(set(a)) == 1:
            pass
        else:
            pass
    else:
        for p in range(n):
            y += (mx - a[p]) // z
    print(y, z)

if __name__ == "__main__":
    alif()