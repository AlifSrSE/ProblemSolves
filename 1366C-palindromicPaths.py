# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    nr, nc = map(int, sys.stdin.readline().split())
    ones_count = [0] * (nr + nc - 1)
    zeros_count = [0] * (nr + nc - 1)

    for r in range(nr):
        row_values = list(map(int, sys.stdin.readline().split()))
        for c in range(nc):
            diagonal_sum = r + c
            if row_values[c] == 1:
                ones_count[diagonal_sum] += 1
            else:
                zeros_count[diagonal_sum] += 1

    total_changes = 0
    num_diagonals = nr + nc - 1
    for p in range(num_diagonals // 2):
        current_ones = ones_count[p] + ones_count[num_diagonals - 1 - p]
        current_zeros = zeros_count[p] + zeros_count[num_diagonals - 1 - p]
        total_changes += min(current_ones, current_zeros)

    sys.stdout.write(str(total_changes) + "\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()