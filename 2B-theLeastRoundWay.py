# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def count_factors(n, p):
    if n == 0:
        return 1
    count = 0
    while n > 0 and n % p == 0:
        count += 1
        n //= p
    return count

def alif():
    n = int(sys.stdin.readline())
    matrix = []
    has_zero = False
    zero_pos = None
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if row[j] == 0:
                has_zero = True
                zero_pos = (i, j)
        matrix.append(row)

    def find_path(dp_matrix, counts_matrix):
        path = []
        i, j = n - 1, n - 1
        while i > 0 or j > 0:
            current_val = dp_matrix[i][j] - counts_matrix[i][j]
            if i > 0 and dp_matrix[i-1][j] == current_val:
                path.append('D')
                i -= 1
            elif j > 0 and dp_matrix[i][j-1] == current_val:
                path.append('R')
                j -= 1
        return ''.join(reversed(path))

    count2 = [[count_factors(matrix[i][j], 2) for j in range(n)] for i in range(n)]
    count5 = [[count_factors(matrix[i][j], 5) for j in range(n)] for i in range(n)]

    dp2 = [[0] * n for _ in range(n)]
    dp5 = [[0] * n for _ in range(n)]

    dp2[0][0] = count2[0][0]
    dp5[0][0] = count5[0][0]

    for i in range(1, n):
        dp2[i][0] = dp2[i-1][0] + count2[i][0]
        dp5[i][0] = dp5[i-1][0] + count5[i][0]

    for j in range(1, n):
        dp2[0][j] = dp2[0][j-1] + count2[0][j]
        dp5[0][j] = dp5[0][j-1] + count5[0][j]

    for i in range(1, n):
        for j in range(1, n):
            dp2[i][j] = min(dp2[i-1][j], dp2[i][j-1]) + count2[i][j]
            dp5[i][j] = min(dp5[i-1][j], dp5[i][j-1]) + count5[i][j]

    zeros_2 = dp2[n-1][n-1]
    zeros_5 = dp5[n-1][n-1]

    if has_zero and min(zeros_2, zeros_5) > 1:
        print(1)
        path = 'D' * zero_pos[0] + 'R' * zero_pos[1]
        path += 'D' * (n - 1 - zero_pos[0]) + 'R' * (n - 1 - zero_pos[1])
        print(path)
    else:
        if zeros_2 < zeros_5:
            print(zeros_2)
            print(find_path(dp2, count2))
        else:
            print(zeros_5)
            print(find_path(dp5, count5))

alif()