# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/14/A

def solve():
    n, m = map(int, input().split())
    drawing = [['0' for _ in range(m)] for _ in range(n)]
    start_row, end_row = n, 0
    start_col, end_col = m, 0

    for row in range(n):
        line = input()
        for col in range(m):
            drawing[row][col] = line[col]
            if line[col] == '*':
                if row < start_row:
                    start_row = row
                if row > end_row:
                    end_row = row
                if col < start_col:
                    start_col = col
                if col > end_col:
                    end_col = col

    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            print(drawing[row][col], end='')
        print()

solve()