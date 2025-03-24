# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1980/D
 
import math

def solve(a):
    n = len(a)

    left_sorted = [False] * n
    left_sorted[0] = True
    if n > 1:
        left_sorted[1] = True
    for i in range(2, n):
        left_sorted[i] = left_sorted[i - 1] and math.gcd(a[i], a[i - 1]) >= math.gcd(a[i - 1], a[i - 2])

    right_sorted = [False] * n
    right_sorted[n - 1] = True
    if n > 1:
        right_sorted[n - 2] = True
    for i in range(n - 3, -1, -1):
        right_sorted[i] = right_sorted[i + 1] and math.gcd(a[i], a[i + 1]) <= math.gcd(a[i + 1], a[i + 2])

    return any(
        (i == 0 or left_sorted[i - 1])
        and (i == n - 1 or right_sorted[i + 1])
        and (i <= 1 or i == n - 1 or math.gcd(a[i - 1], a[i + 1]) >= math.gcd(a[i - 1], a[i - 2]))
        and (i >= n - 2 or i == 0 or math.gcd(a[i - 1], a[i + 1]) <= math.gcd(a[i + 1], a[i + 2]))
        for i in range(n)
    )

if __name__ == "__main__":
    sc = int(input())
    for _ in range(sc):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if solve(a) else "NO")