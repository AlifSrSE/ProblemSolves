# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/C

from sys import stdin
input = stdin.readline

def main():
    t = int(input().strip())
    
    for _ in range(t):
        input().strip()
        grid = [input().strip() for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if grid[i][j] == '#':
                    cnt = 0
                    if i >= 1 and j >= 1 and grid[i-1][j-1] == '#':
                        cnt += 1
                    if i >= 1 and j + 1 < 8 and grid[i-1][j+1] == '#':
                        cnt += 1
                    if i + 1 < 8 and j >= 1 and grid[i+1][j-1] == '#':
                        cnt += 1
                    if i + 1 < 8 and j + 1 < 8 and grid[i+1][j+1] == '#':
                        cnt += 1
                    if cnt == 4:
                        print(f"{i + 1} {j + 1}")
                        break
            else:
                continue
            break

if __name__ == "__main__":
    main()