# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1316/problem/D

import sys
from collections import deque

def alif():
    try:
        n = int(sys.stdin.readline())
        dest = []
        for _ in range(n):
            row_data = list(map(int, sys.stdin.readline().split()))
            dest_row = []
            for j in range(0, 2 * n, 2):
                dest_row.append((row_data[j], row_data[j+1]))
            dest.append(dest_row)

        ans = [['' for _ in range(n)] for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if dest[r][c] == (r + 1, c + 1):
                    ans[r][c] = 'X'
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            neighbors = [
                (r - 1, c, 'D'),
                (r + 1, c, 'U'),
                (r, c - 1, 'R'),
                (r, c + 1, 'L')
            ]

            for nr, nc, char_to_set in neighbors:
                if 0 <= nr < n and 0 <= nc < n and ans[nr][nc] == '':
                    if dest[nr][nc] == dest[r][c]:
                        ans[nr][nc] = char_to_set
                        q.append((nr, nc))
        is_valid = True

        for r in range(n):
            for c in range(n):
                if ans[r][c] == '':
                    if dest[r][c] != (-1, -1):
                        is_valid = False
                        break
                    found_neighbor = False
                    neighbors = [
                        (r - 1, c, 'U'),
                        (r + 1, c, 'D'),
                        (r, c - 1, 'L'),
                        (r, c + 1, 'R')
                    ]

                    for nr, nc, char_to_set in neighbors:
                        if 0 <= nr < n and 0 <= nc < n and dest[nr][nc] == (-1, -1):
                            ans[r][c] = char_to_set
                            found_neighbor = True
                            break
                    
                    if not found_neighbor:
                        is_valid = False
                        break
            if not is_valid:
                break
        if is_valid:
            print("VALID")
            for row in ans:
                print("".join(row))
        else:
            print("INVALID")

    except (IOError, ValueError):
        print("INVALID")

if __name__ == "__main__":
    alif()