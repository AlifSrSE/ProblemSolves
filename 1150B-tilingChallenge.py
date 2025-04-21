# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/1150/problem/B

R_OFFSETS = [0, 1, 1, 1, 2]
C_OFFSETS = [0, -1, 0, 1, 0]

def main():
    n = int(input())
    board = [list(input()) for _ in range(n)]

    if _(board):
        print("YES")
    else:
        print("NO")

def _(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == '.' and not fill(board, r, c):
                return False
    return True

def fill(board, top_r, top_c):
    n = len(board)
    for i in range(len(R_OFFSETS)):
        r = top_r + R_OFFSETS[i]
        c = top_c + C_OFFSETS[i]
        if not (0 <= r < n and 0 <= c < n and board[r][c] == '.'):
            return False
        board[r][c] = '#'
    return True

if __name__ == "__main__":
    main()
