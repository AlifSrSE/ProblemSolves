# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/17/B

def solve():
    n = int(input())
    for _ in range(n):
        input()

    m = int(input())
    cost = {}
    for _ in range(m):
        x, y, c = map(int, input().split())
        if y in cost:
            cost[y] = min(cost[y], c)
        else:
            cost[y] = c

    if len(cost) < n - 1:
        print("-1")
        return

    total = sum(cost.values())
    print(total)

solve()