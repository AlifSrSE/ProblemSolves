#Author: AlifSrSE

import sys

def solve(n):
    lines = ["2"]
    for i in range(n - 1):
        val1 = n - i - 1
        val2 = min(n, n - i + 1)
        lines.append(f"{val1} {val2}")
    return "\n".join(lines)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for tc in range(1, t + 1):
        n = int(input_data[tc])
        results.append(solve(n))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()