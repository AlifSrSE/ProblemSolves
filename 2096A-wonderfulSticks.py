# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/2096/problem/A

import sys

def generate_arrangement(n, pattern):
    left_count = pattern.count('<')
    right_count = pattern.count('>')

    left_pool = list(range(1, left_count + 1))
    right_pool = list(range(n - right_count + 1, n + 1))
    available = set(range(1, n + 1))
    middle_value = (available - set(left_pool) - set(right_pool)).pop()
    requirements = ['L' if ch == '<' else 'R' for ch in pattern]

    result = [None] * n
    result[0] = middle_value
    idx = 1

    ptr = 0
    while ptr < len(requirements):
        current_type = requirements[ptr]
        end_ptr = ptr
        while end_ptr < len(requirements) and requirements[end_ptr] == current_type:
            end_ptr += 1
        segment_length = end_ptr - ptr

        if current_type == 'L':
            selected = left_pool[-segment_length:]
            left_pool = left_pool[:-segment_length]
            for num in reversed(sorted(selected)):
                result[idx] = num
                idx += 1
        else:
            selected = right_pool[:segment_length]
            right_pool = right_pool[segment_length:]
            for num in sorted(selected):
                result[idx] = num
                idx += 1

        ptr = end_ptr

    return result

def main():
    input = sys.stdin.readline
    test_cases = int(input())
    for _ in range(test_cases):
        num_sticks = int(input())
        comparison_string = input().strip()
        arrangement = generate_arrangement(num_sticks, comparison_string)
        print(' '.join(map(str, arrangement)))

if __name__ == "__main__":
    main()
