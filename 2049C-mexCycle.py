# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/2049/C

def solve():
    t = int(input())
    for _ in range(t):
        n, x, y = map(int, input().split())
        x -= 1
        y -= 1
        v = [0] * n
        for p in range(n):
            v[(x + p) % n] = p % 2
        if n % 2 == 0 or (x - y) % 2 == 0:
            v[x] = 2
        print(*v)

solve()