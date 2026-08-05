# Author: AlifSrSE
import sys

def solve(x):
    # Ensure x is sorted for the greedy check
    x.sort()
    for i in range(1, len(x)):
        if x[i] <= x[i - 1]:
            x[i] += 1
    return len(set(x))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        x = [int(val) for val in input_data[ptr + 1 : ptr + 1 + n]]
        results.append(str(solve(x)))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()