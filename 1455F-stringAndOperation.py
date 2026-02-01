# Author: AlifSrSE

import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()

        possible = [[False]*n for _ in range(n)]

        for i in range(n):
            for j in (i-1, i, i+1):
                if 0 <= j < n:
                    possible[i][j] = True

        used = [False]*n
        result = ['']*n

        for j in range(n):
            for c in range(n):
                if not used[c] and possible[c][j]:
                    used[c] = True
                    result[j] = 'a'
                    break

        print("".join(result))

if __name__ == "__main__":
    solve()
