# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        n = int(sys.stdin.readline())
        grid = [sys.stdin.readline().strip() for _ in range(n)]
        possible = True
        
        for r in range(n - 1):
            for c in range(n - 1):
                if grid[r][c] == '1':
                    if grid[r + 1][c] == '0' and grid[r][c + 1] == '0':
                        possible = False
                        break
            if not possible:
                break
        
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()