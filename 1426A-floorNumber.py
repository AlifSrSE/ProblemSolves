#Author: AlifSrSE

import sys

def solve(n, x):
    return 1 if n <= 2 else (n - 2 + x - 1) // x + 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        x = int(input_data[ptr+1])
        results.append(str(solve(n, x)))
        ptr += 2
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()