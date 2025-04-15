# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    x, n, m = map(int, input().split())
    min_x = x
    max_x = x
    cn = n
    cm = m
    while min_x > 1 and n + m > 0:
        if min_x % 2 == 0:
            if m > 0:
                m -= 1
            else:
                n -= 1
            min_x //= 2
        else:
            if m > 0:
                min_x = min_x // 2 + 1
                m -= 1
            else:
                min_x //= 2
                n -= 1
    if n > 0:
        min_x = 0
    n = cn
    m = cm
    while max_x > 1 and n + m > 0:
        if max_x % 2 == 0:
            if n > 0:
                n -= 1
            else:
                m -= 1
            max_x //= 2
        else:
            if n > 0:
                max_x //= 2
                n -= 1
            else:
                max_x = max_x // 2 + 1
                m -= 1
    if n > 0:
        max_x = 0
    print(min_x, max_x)

if __name__ == "__main__":
    _t = int(input())
    for _ in range(_t):
        solve()