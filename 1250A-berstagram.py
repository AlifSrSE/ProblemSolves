# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1250/problem/A

import sys

def alif():
    n, m = map(int, sys.stdin.readline().split())
    which = [0] * (n + 1)
    where = [0] * (n + 1)
    top = [0] * (n + 1)
    bottom = [0] * (n + 1)

    for p in range(1, n + 1):
        top[p] = p
        bottom[p] = p
        which[p] = p
        where[p] = p

    operations = list(map(int, sys.stdin.readline().split()))

    for x in operations:
        pos = where[x]

        if pos <= 1:
            continue

        y = which[pos - 1]
        where[x] = pos - 1
        which[pos - 1] = x
        where[y] = pos
        which[pos] = y
        top[x] = min(top[x], where[x])
        bottom[y] = max(bottom[y], where[y])

    for p in range(1, n + 1):
        sys.stdout.write(f"{top[p]} {bottom[p]}\n")

if __name__ == "__main__":
    alif()