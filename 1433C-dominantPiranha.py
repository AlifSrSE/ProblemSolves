#Author: AlifSrSE

import sys

def solve(a):
    if not a:
        return -1
    max_val = max(a)
    n = len(a)
    for i in range(n):
        if a[i] == max_val:
            if (i > 0 and a[i-1] != max_val) or (i < n - 1 and a[i+1] != max_val):
                return i + 1
    return -1

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