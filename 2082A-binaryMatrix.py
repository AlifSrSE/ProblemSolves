# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(matrix):
    n = len(matrix)
    m = len(matrix[0])

    def compute_xor(values):
        result = 0
        for value in values:
            result ^= value
        return result

    row_xors = [compute_xor(row) for row in matrix]
    col_xors = [compute_xor([matrix[r][c] for r in range(n)]) for c in range(m)]

    return max(sum(1 for x in row_xors if x == 1), sum(1 for x in col_xors if x == 1))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        matrix = []
        for _ in range(n):
            line = input()
            matrix.append([int(c) for c in line])

        print(solve(matrix))