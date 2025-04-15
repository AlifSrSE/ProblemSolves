# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/15/A

def solve():
    n, t = map(int, input().split())
    v = []
    for _ in range(n):
        x, a = map(float, input().split())
        v.append((x - a / 2.0, x + a / 2.0))
    v.sort()

    count = 2
    for p in range(1, n):
        diff = v[p][0] - v[p - 1][1]
        count += 2 * (diff > t) + (diff == t)

    print(count)

solve()