#Author: AlifSrSE

import sys

MODULUS = 1_000_000_007

def multiply_mod(x, y):
    return (x * y) % MODULUS

def solve(n, x, pos):
    left_count = x - 1
    right_count = n - 1 - left_count

    result = 1
    left = 0
    right = n
    while left < right:
        middle = (left + right) // 2
        if middle <= pos:
            if middle != pos:
                result = multiply_mod(result, left_count)
                left_count -= 1
            left = middle + 1
        else:
            result = multiply_mod(result, right_count)
            right_count -= 1
            right = middle

    for i in range(1, left_count + right_count + 1):
        result = multiply_mod(result, i)

    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    x = int(input_data[1])
    pos = int(input_data[2])
    print(solve(n, x, pos))

if __name__ == "__main__":
    main()