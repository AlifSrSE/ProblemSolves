# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1999/E
 
def solve(l, r):
    operation_num_to_count = {}
    operation_num = 1
    begin = 1
    end = 3
    while True:
        lower = max(l, begin)
        upper = min(r, end - 1)
        if lower <= upper:
            operation_num_to_count[operation_num] = upper - lower + 1

        if end > r:
            break

        operation_num += 1
        begin *= 3
        end *= 3

    min_operation_num = min(operation_num_to_count.keys())
    total_sum = sum(o * operation_num_to_count[o] for o in operation_num_to_count.keys())

    return min_operation_num + total_sum

if __name__ == "__main__":
    sc = int(input())
    for _ in range(sc):
        l, r = map(int, input().split())
        print(solve(l, r))