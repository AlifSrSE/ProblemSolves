# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/18/C

def solve():
    n = int(input())
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    left_sum = 0
    ways = 0

    for k in range(n - 1):
        left_sum += numbers[k]
        if 2 * left_sum == total:
            ways += 1

    print(ways)

solve()