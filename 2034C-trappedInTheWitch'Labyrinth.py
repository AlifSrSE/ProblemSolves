# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/2034/C

def solve(maze):
    n = len(maze)
    m = len(maze[0])

    escaped = build_escaped(maze)

    result = 0
    r_offsets = [-1, 0, 1, 0]
    c_offsets = [0, 1, 0, -1]

    for r in range(n):
        for c in range(m):
            if not escaped[r][c] and any(
                0 <= r + r_offsets[i] < n
                and 0 <= c + c_offsets[i] < m
                and not escaped[r + r_offsets[i]][c + c_offsets[i]]
                for i in range(4)
            ):
                result += 1

    return result


def build_escaped(maze):
    n = len(maze)
    m = len(maze[0])

    escaped = [False] * (n * m)

    adj_lists = [[] for _ in range(n * m)]
    direction_to_index = {"U": 0, "D": 2, "L": 3, "R": 1}

    for r in range(n):
        for c in range(m):
            if maze[r][c] != "?":
                index = direction_to_index[maze[r][c]]
                adj_r = r + R_OFFSETS[index]
                adj_c = c + C_OFFSETS[index]
                if 0 <= adj_r < n and 0 <= adj_c < m:
                    adj_lists[to_index(m, adj_r, adj_c)].append(to_index(m, r, c))
                else:
                    escaped[to_index(m, r, c)] = True

    for i in range(len(escaped)):
        if escaped[i]:
            search(escaped, adj_lists, i)

    result = [[False] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            result[r][c] = escaped[to_index(m, r, c)]

    return result


def to_index(m, r, c):
    return r * m + c


def search(escaped, adj_lists, node):
    for adj in adj_lists[node]:
        if not escaped[adj]:
            escaped[adj] = True
            search(escaped, adj_lists, adj)


if __name__ == "__main__":
    t = int(input())
    R_OFFSETS = [-1, 0, 1, 0]
    C_OFFSETS = [0, 1, 0, -1]

    for _ in range(t):
        n, m = map(int, input().split())
        maze = [input() for _ in range(n)]
        print(solve([[char for char in row] for row in maze]))