# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/263/A

def solve():
    dim = 5
    row, col = 0, 0
    for i in range(dim):
        line = list(map(int, input().split()))
        for j in range(dim):
            if line[j] == 1:
                row, col = i, j
                break
        if row != 0 or col != 0:
            break
    print(abs(row - 2) + abs(col - 2))

solve()