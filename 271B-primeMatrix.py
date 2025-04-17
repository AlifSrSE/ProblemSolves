# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/271/B

import math

def sieve(upper_bound):
    is_prime = [True] * upper_bound
    if upper_bound > 0:
        is_prime[0] = False
    if upper_bound > 1:
        is_prime[1] = False
    for k in range(2, int(math.sqrt(upper_bound)) + 1):
        if is_prime[k]:
            for m in range(k * k, upper_bound, k):
                is_prime[m] = False
    return is_prime

def solve():
    num_rows, num_cols = map(int, input().split())
    prime_gap = 100
    numbers = []
    current_max = 0
    for _ in range(num_rows):
        row = list(map(int, input().split()))
        numbers.append(row)
        for val in row:
            if val > current_max:
                current_max = val

    upper_bound = current_max + prime_gap + 1
    is_prime = sieve(upper_bound)

    for row in range(num_rows):
        for col in range(num_cols):
            diff = 0
            num = numbers[row][col]
            while num < upper_bound and not is_prime[num]:
                diff += 1
                num += 1
            numbers[row][col] = diff

    min_moves = num_rows * num_cols * prime_gap

    for row in range(num_rows):
        total = sum(numbers[row])
        if total < min_moves:
            min_moves = total

    for col in range(num_cols):
        total = 0
        for row in range(num_rows):
            total += numbers[row][col]
        if total < min_moves:
            min_moves = total

    print(min_moves)

if __name__ == "__main__":
    solve()