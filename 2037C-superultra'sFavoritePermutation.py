# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/2037/C

def solve(n):
    if n <= 4:
        return "-1"

    even_nums = [x for x in range(1, n + 1) if x % 2 == 0 and x != 4]
    odd_nums = [x for x in range(1, n + 1) if x % 2 == 1 and x != 5]

    result = even_nums + [4] + [5] + odd_nums
    return " ".join(map(str, result))

t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))