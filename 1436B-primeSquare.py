#Author: AlifSrSE

import sys

def solve(n):
    square = [[0] * n for _ in range(n)]
    for i in range(n):
        square[i][i] = 1
        square[i][n - 1 - i] = 1

    if n % 2 != 0:
        mid = n // 2
        for i in range(-1, 2):
            for j in range(-1, 2):
                square[mid + i][mid + j] = 1

    return "\n".join(" ".join(map(str, row)) for row in square)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(solve(n))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()