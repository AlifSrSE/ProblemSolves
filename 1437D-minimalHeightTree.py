#Author: AlifSrSE

import sys

def solve(a):
    if len(a) <= 1: return 0
    result = 1
    parent_num = 1
    next_parent_num = 1
    parent_index = 0
    for i in range(2, len(a)):
        if a[i] > a[i - 1]:
            next_parent_num += 1
        elif parent_index != parent_num - 1:
            next_parent_num += 1
            parent_index += 1
        else:
            parent_num = next_parent_num
            next_parent_num = 1
            parent_index = 0
            result += 1
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t_cases = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t_cases):
        n = int(input_data[ptr])
        a = [int(x) for x in input_data[ptr+1 : ptr+1+n]]
        results.append(str(solve(a)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()