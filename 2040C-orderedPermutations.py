# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2040/C

def solve():
    n, k = map(int, input().split())
    if n < 45 and k > (1 << (n - 1)):
        print(-1)
        return

    k -= 1
    bit = []
    while k:
        bit.append(k % 2)
        k //= 2
    while len(bit) < n - 1:
        bit.append(0)

    r = []
    for i, c in zip(range(n - 2, -1, -1), range(1, n)):
        if bit[i] == 0:
            print(c, end=' ')
        else:
            r.append(c)
    print(n, end=' ')
    r.reverse()
    for i in r:
        print(i, end=' ')
    print()

t = int(input())
for _ in range(t):
    solve()