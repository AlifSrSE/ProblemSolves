#Author: AlifSrSE

import sys

def solve(n):
    result = n - 1
    i = 2
    while i - 1 < result:
        result = min(result, i - 1 + (n + i - 1) // i - 1)
        i += 1
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(str(solve(n)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()