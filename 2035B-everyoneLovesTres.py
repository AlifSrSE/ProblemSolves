# Author: AlifSrSe
# date: 2025-03-27
# https://codeforces.com/problemset/problem/2035/B

def solve():
    n = int(input())
    if n % 2 == 0:
        return "3" * (n - 2) + "66"
    if n <= 3:
        return "-1"
    return "3" * (n - 5) + "36366"

t = int(input())
for _ in range(t):
    print(solve())