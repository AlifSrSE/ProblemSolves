# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1292/problem/A

import sys

def alif():
    try:
        n, q = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return

    s = [[False] * n for _ in range(2)]
    cnt = 0

    while q > 0:
        try:
            row, col = map(int, sys.stdin.readline().split())
            row -= 1
            col -= 1
        except (IOError, ValueError):
            q -= 1
            continue

        if s[row][col]:
            if s[1 - row][col]:
                cnt -= 1
            if col > 0 and s[1 - row][col - 1]:
                cnt -= 1
            if col + 1 < n and s[1 - row][col + 1]:
                cnt -= 1
        else:
            if s[1 - row][col]:
                cnt += 1
            if col > 0 and s[1 - row][col - 1]:
                cnt += 1
            if col + 1 < n and s[1 - row][col + 1]:
                cnt += 1
        
        s[row][col] = not s[row][col]

        if cnt == 0:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")
        q -= 1

if __name__ == "__main__":
    alif()