#Author: AlifSrSE

import sys

def solve(a):
    indices = [i for i, val in enumerate(a) if val == 1]
    if not indices:
        return 0
    min_one_index = min(indices)
    max_one_index = max(indices)
    return a[min_one_index:max_one_index+1].count(0)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        a = [int(x) for x in input_data[ptr + 1 : ptr + 1 + n]]
        results.append(str(solve(a)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()