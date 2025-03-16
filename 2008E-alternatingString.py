# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/E

def solve(s):
    letter_to_count_maps = [{}, {}]
    for i, char in enumerate(s):
        letter_to_count_maps[i % 2][char] = letter_to_count_maps[i % 2].get(char, 0) + 1

    if len(s) % 2 == 0:
        return compute_operation_num(len(s), letter_to_count_maps)

    result = float('inf')
    for i in range(len(s) - 1, -1, -1):
        letter_to_count_maps[i % 2][s[i]] -= 1
        if letter_to_count_maps[i % 2][s[i]] == 0:
            del letter_to_count_maps[i % 2][s[i]]

        result = min(result, 1 + compute_operation_num(len(s) - 1, letter_to_count_maps))

        letter_to_count_maps[1 - i % 2][s[i]] = letter_to_count_maps[1 - i % 2].get(s[i], 0) + 1

    return result

def compute_operation_num(length, letter_to_count_maps):
    return compute_operation_num_for_half(length // 2, letter_to_count_maps[0]) + \
           compute_operation_num_for_half(length // 2, letter_to_count_maps[1])

def compute_operation_num_for_half(half_length, letter_to_count):
    if not letter_to_count:
        return half_length
    return half_length - max(letter_to_count.values())

t = int(input())
for _ in range(t):
    input() 
    s = input()
    print(solve(s))