# Author : AlifSrSE
# Date : 2025-03-28
# Problem link : https://codeforces.com/contest/2053/problem/B

def find_left_index(sorted_fixed_values, min_value):
    result = len(sorted_fixed_values)
    lower = 0
    upper = len(sorted_fixed_values) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if sorted_fixed_values[middle] >= min_value:
            result = middle
            upper = middle - 1
        else:
            lower = middle + 1
    return result

def find_right_index(sorted_fixed_values, max_value):
    result = -1
    lower = 0
    upper = len(sorted_fixed_values) - 1
    while lower <= upper:
        middle = (lower + upper) // 2
        if sorted_fixed_values[middle] <= max_value:
            result = middle
            lower = middle + 1
        else:
            upper = middle - 1
    return result

def solve(l, r):
    fixed_value_to_count = {}
    for i in range(len(l)):
        if l[i] == r[i]:
            fixed_value_to_count[l[i]] = fixed_value_to_count.get(l[i], 0) + 1

    sorted_fixed_values = sorted(fixed_value_to_count.keys())

    result = ""
    for i in range(len(l)):
        if l[i] == r[i]:
            if fixed_value_to_count.get(l[i]) == 1:
                result += "1"
            else:
                result += "0"
        else:
            if r[i] - l[i] > find_right_index(sorted_fixed_values, r[i]) - find_left_index(sorted_fixed_values, l[i]):
                result += "1"
            else:
                result += "0"
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    r = []
    for _ in range(n):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    print(solve(l, r))