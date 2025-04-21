# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/2096/problem/C

import sys
input = sys.stdin.readline

MAX_COST = 10**30

def compute_min_cost(n, grid, row_costs, col_costs):
    row_rules = [[[False] * 2 for _ in range(2)] for _ in range(n - 1)]
    col_rules = [[[False] * 2 for _ in range(2)] for _ in range(n - 1)]

    for i in range(n - 1):
        for j in range(n):
            diff = grid[i][j] - grid[i + 1][j]
            if diff == 0:
                row_rules[i][0][0] = True
                row_rules[i][1][1] = True
            elif diff == 1:
                row_rules[i][0][1] = True
            elif diff == -1:
                row_rules[i][1][0] = True

    for j in range(n - 1):
        for i in range(n):
            diff = grid[i][j] - grid[i][j + 1]
            if diff == 0:
                col_rules[j][0][0] = True
                col_rules[j][1][1] = True
            elif diff == 1:
                col_rules[j][0][1] = True
            elif diff == -1:
                col_rules[j][1][0] = True

    dp_rows = [[MAX_COST, MAX_COST] for _ in range(n)]
    dp_rows[0][0] = 0
    dp_rows[0][1] = row_costs[0]
    for i in range(1, n):
        for cur in (0, 1):
            min_cost = MAX_COST
            for prev in (0, 1):
                if not row_rules[i - 1][prev][cur]:
                    prior = dp_rows[i - 1][prev]
                    cost = prior + (cur * row_costs[i])
                    min_cost = min(min_cost, cost)
            dp_rows[i][cur] = min_cost

    min_row_cost = min(dp_rows[n - 1])
    if min_row_cost >= MAX_COST:
        return -1

    dp_cols = [[MAX_COST, MAX_COST] for _ in range(n)]
    dp_cols[0][0] = 0
    dp_cols[0][1] = col_costs[0]
    for j in range(1, n):
        for cur in (0, 1):
            min_cost = MAX_COST
            for prev in (0, 1):
                if not col_rules[j - 1][prev][cur]:
                    prior = dp_cols[j - 1][prev]
                    cost = prior + (cur * col_costs[j])
                    min_cost = min(min_cost, cost)
            dp_cols[j][cur] = min_cost

    min_col_cost = min(dp_cols[n - 1])
    if min_col_cost >= MAX_COST:
        return -1

    return min_row_cost + min_col_cost

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        row_prices = list(map(int, input().split()))
        col_prices = list(map(int, input().split()))
        answer = compute_min_cost(N, matrix, row_prices, col_prices)
        results.append(str(answer))
    print("\n".join(results))

if __name__ == "__main__":
    main()
