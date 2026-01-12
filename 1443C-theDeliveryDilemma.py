#Author: AlifSrSE

import sys

def check(a, b, time):
    needed = 0
    for i in range(len(a)):
        if a[i] > time:
            needed += b[i]
    return needed <= time

def solve(a, b):
    result = -1
    lower = 0
    upper = max(a) if a else 0
    while lower <= upper:
        middle = (lower + upper) // 2
        if check(a, b, middle):
            result = middle
            upper = middle - 1
        else:
            lower = middle + 1
    return result

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
        b = [int(x) for x in input_data[ptr + 1 + n : ptr + 1 + 2*n]]
        results.append(str(solve(a, b)))
        ptr += 1 + 2*n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
    