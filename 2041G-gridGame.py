# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from collections import defaultdict

def solve_case(n, q, lines):
    col_blocks = defaultdict(list)
    
    for y, s, f in lines:
        col_blocks[y].append((s, f))

    for y in col_blocks:
        intervals = sorted(col_blocks[y])
        merged = []
        for s, f in intervals:
            if not merged or merged[-1][1] < s - 1:
                merged.append([s, f])
            else:
                merged[-1][1] = max(merged[-1][1], f)
        col_blocks[y] = merged

    white_segments = defaultdict(list)

    for y in col_blocks:
        last = 1
        for s, f in col_blocks[y]:
            if last < s:
                white_segments[y].append((last, s - 1))
            last = f + 1
        if last <= n:
            white_segments[y].append((last, n))

    black_columns = set(col_blocks.keys())
    all_columns = sorted(set(col_blocks.keys()))
    
    total_disconnections = 0

    considered_columns = set(all_columns)
    for col in all_columns:
        if col > 1:
            considered_columns.add(col - 1)
        if col < n:
            considered_columns.add(col + 1)

    considered_columns = sorted(considered_columns)

    for y in considered_columns:
        if y in white_segments:
            for r1, r2 in white_segments[y]:
                for x in range(r1, r2 + 1):
                    connections = 0
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 1 <= nx <= n and 1 <= ny <= n:
                            if ny in white_segments:
                                for a, b in white_segments[ny]:
                                    if a <= nx <= b:
                                        connections += 1
                                        break
                            else:
                                connections += 1
                    if connections >= 2:
                        total_disconnections += 1

        else:
            for x in range(1, n+1):
                connections = 0
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if ny in white_segments:
                            for a, b in white_segments[ny]:
                                if a <= nx <= b:
                                    connections += 1
                                    break
                        else:
                            connections += 1
                if connections >= 2:
                    total_disconnections += 1

    return total_disconnections


def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        lines = [tuple(map(int, input().split())) for _ in range(q)]
        print(solve_case(n, q, lines))

if __name__ == "__main__":
    main()
