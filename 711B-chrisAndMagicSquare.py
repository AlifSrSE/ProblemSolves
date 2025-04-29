# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/711/problem/B

def solve():
    n = int(input())
    grid = []
    empty_row, empty_col = -1, -1
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
        if 0 in row:
            empty_row = i
            empty_col = row.index(0)

    if n == 1:
        print(1)
        return

    first_full_row_sum = -1
    for i in range(n):
        if i != empty_row:
            row_sum = sum(grid[i])
            first_full_row_sum = row_sum
            break

    if first_full_row_sum == -1:
        print(-1)
        return

    current_empty_row_sum = sum(grid[empty_row])
    fill_value = first_full_row_sum - current_empty_row_sum

    if fill_value <= 0:
        print(-1)
        return

    grid[empty_row][empty_col] = fill_value

    for row in grid:
        if sum(row) != first_full_row_sum:
            print(-1)
            return

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += grid[i][j]
        if col_sum != first_full_row_sum:
            print(-1)
            return

    main_diag_sum = 0
    for i in range(n):
        main_diag_sum += grid[i][i]
    if main_diag_sum != first_full_row_sum:
        print(-1)
        return

    sec_diag_sum = 0
    for i in range(n):
        sec_diag_sum += grid[i][n - 1 - i]
    if sec_diag_sum != first_full_row_sum:
        print(-1)
        return

    print(fill_value)

if __name__ == "__main__":
    solve()