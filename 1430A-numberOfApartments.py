#Author: AlifSrSE

import sys

def solve(n):
    for k in range(n // 7 + 1):
        for j in range((n - k * 7) // 5 + 1):
            rem = n - k * 7 - j * 5
            if rem >= 0 and rem % 3 == 0:
                i = rem // 3
                return f"{i} {j} {k}"
    return "-1"

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