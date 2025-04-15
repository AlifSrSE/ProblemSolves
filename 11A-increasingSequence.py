# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/11/A

def solve():
    n, d = map(int, input().split())
    values = list(map(int, input().split()))
    current = -1
    total = 0

    for temp in values:
        if current < temp:
            current = temp
        else:
            times = 1 + (current - temp) // d
            current = temp + times * d
            total += times

    print(total)

solve()