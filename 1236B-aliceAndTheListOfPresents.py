# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def big(x, y, md):
    if y == 0:
        return 1
    if y % 2:
        return (x * big(x, y - 1, md)) % md
    else:
        temp = big(x, y // 2, md)
        return (temp * temp) % md

def solve():
    n, m = map(int, input().split())
    md = 10**7
    result = big(big(2, m, md) - 1, n, md) % md
    print(result)

solve()