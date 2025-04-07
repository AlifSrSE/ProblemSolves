# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    mg = [["" for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        row = input()
        for j in range(1, m + 1):
            mg[i][j] = row[j - 1]

    res = []
    v = []
    k = 0

    def add(a, x, y):
        nonlocal k
        res.append(a)
        v.append((x, y))
        mg[x][y] = a
        k += 1

    dir_offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x, y, dep):
        add('B', x, y)
        for dx_offset, dy_offset in dir_offsets:
            dx = x + dx_offset
            dy = y + dy_offset
            if 1 <= dx <= n and 1 <= dy <= m and mg[dx][dy] == '.':
                dfs(dx, dy, dep + 1)
        if dep > 0:
            add('D', x, y)
            add('R', x, y)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if mg[i][j] == '.':
                dfs(i, j, 0)

    print(k)
    for i in range(k):
        print(f"{res[i]} {v[i][0]} {v[i][1]}")

if __name__ == "__main__":
    solve()