#Author: AlifSrSE

import sys

def solve(a):
    total_sum = sum(a)
    negatives = [x for x in a if x < 0]
    positives = [x for x in a if x > 0]
    zeros = [x for x in a if x == 0]

    if total_sum < 0:
        res = negatives + positives + zeros
        return f"YES\n{' '.join(map(str, res))}"
    elif total_sum > 0:
        res = positives + negatives + zeros
        return f"YES\n{' '.join(map(str, res))}"
    else:
        return "NO"

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
        results.append(solve(a))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()