# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/16/C

def gcd(x, y):
    return y if x == 0 else gcd(y % x, x)

def solve():
    a, b, x, y = map(int, input().split())
    g = gcd(x, y)
    x //= g
    y //= g
    u = a // x
    v = b // y
    factor = min(u, v)
    print(factor * x, factor * y)

solve()