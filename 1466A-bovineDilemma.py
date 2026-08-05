# Author: AlifSrSE
import sys

def solve(x):
    differences = set()
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            differences.add(x[j] - x[i])
    return len(differences)

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