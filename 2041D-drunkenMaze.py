# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from collections import deque
import sys
input = sys.stdin.readline

nxt = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def solve():
    n, m = map(int, input().split())
    ss = []
    sp = ep = (0, 0)

    for i in range(n):
        s = input().strip()
        ss.append(s)
        for j in range(m):
            if s[j] == 'S':
                sp = (i, j)
            elif s[j] == 'T':
                ep = (i, j)

    INF = 1_000_000_000
    dis = [[[[INF for _ in range(m)] for _ in range(4)] for _ in range(4)] for _ in range(n)]
    Q = deque()

    for i in range(4):
        x = sp[0] + nxt[i][0]
        y = sp[1] + nxt[i][1]
        if 0 <= x < n and 0 <= y < m and ss[x][y] != '#':
            dis[x][i][1][y] = 1
            Q.append((x, i, 1, y))

    while Q:
        x, d, l, y = Q.popleft()
        for i in range(4):
            nx = x + nxt[i][0]
            ny = y + nxt[i][1]
            if 0 <= nx < n and 0 <= ny < m and ss[nx][ny] != '#':
                nl = l + 1 if d == i else 1
                if d == i and nl > 3:
                    continue
                if dis[nx][i][nl][ny] >= INF:
                    dis[nx][i][nl][ny] = dis[x][d][l][y] + 1
                    Q.append((nx, i, nl, ny))

    res = INF
    ex, ey = ep
    for i in range(4):
        for j in range(4):
            res = min(res, dis[ex][i][j][ey])

    print(res if res < INF - 1000 else -1)


def main():
    T = 1
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
