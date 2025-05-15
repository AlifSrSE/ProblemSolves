# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/275/A

def solve():
    dim = 3
    state = [[0 for _ in range(dim)] for _ in range(dim)]

    for row in range(dim):
        row_input = list(map(int, input().split()))
        for col in range(dim):
            temp = row_input[col]
            state[row][col] += temp
            if row > 0:
                state[row - 1][col] += temp
            if col > 0:
                state[row][col - 1] += temp
            if row < dim - 1:
                state[row + 1][col] += temp
            if col < dim - 1:
                state[row][col + 1] += temp

    for row in range(dim):
        for col in range(dim):
            print((1 + state[row][col]) % 2, end="")
        print()

if __name__ == "__main__":
    solve()