# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/22/B

def solve():
    n, m = map(int, input().split())
    rv = [input() for _ in range(n)]

    max_perim = 0
    for length in range(1, n + 1):
        for width in range(1, m + 1):
            for srow in range(n):
                if srow + length > n:
                    continue
                for scol in range(m):
                    if scol + width > m:
                        continue

                    possible = True
                    for row in range(length):
                        if not possible:
                            break
                        for col in range(width):
                            if rv[srow + row][scol + col] == '1':
                                possible = False
                                break

                    if possible:
                        perim = 2 * (length + width)
                        max_perim = max(max_perim, perim)

    print(max_perim)

solve()