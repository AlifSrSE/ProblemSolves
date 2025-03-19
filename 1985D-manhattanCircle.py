# Author : AlifSrSE
# Date : 2025-03-18
# Problem link : https://codeforces.com/contest/1985/problem/D

def solve():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    
    row = 0
    col = 0
    each_row = 0
    
    for i in range(n):
        cnt = s[i].count('#')
        if cnt > each_row:
            each_row = cnt
            row = i
    
    each_col = 0
    for j in range(m):
        cnt = 0
        for i in range(n):
            if s[i][j] == '#':
                cnt += 1
        if cnt > each_col:
            each_col = cnt
            col = j
    
    print(row + 1, col + 1)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()