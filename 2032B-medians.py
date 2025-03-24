# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2032/B

def solve():
    n, k = map(int, input().split())
    if n == 1:
        print(1)
        print(1)
        return
    left = k - 1
    right = n - k
    if (left % 2) and (right % 2):
        print(3)
        print(1, k, k + 1)
    else:
        left -= 1
        right -= 1
        if left > 0 and right > 0:
            print(3)
            print(1, k - 1, k + 2)
        else:
            print(-1)

t = int(input())
for _ in range(t):
    solve()