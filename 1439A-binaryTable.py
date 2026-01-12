#Author: AlifSrSE

import sys

def add_operation(operations, r1, c1, r2, c2, r3, c3):
    operations.append(f"{r1 + 1} {c1 + 1} {r2 + 1} {c2 + 1} {r3 + 1} {c3 + 1}")

def solve(table):
    n = len(table)
    m = len(table[0])
    operations = []
    for r in range(n):
        for c in range(m):
            if table[r][c] == '1':
                adj_r = r - 1 if r == n - 1 else r + 1
                adj_c = c - 1 if c == m - 1 else c + 1

                add_operation(operations, r, c, adj_r, adj_c, r, adj_c)
                add_operation(operations, r, c, adj_r, adj_c, adj_r, c)
                add_operation(operations, r, c, r, adj_c, adj_r, c)
                
    return f"{len(operations)}\n" + "\n".join(operations)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr+1])
        ptr += 2
        table = []
        for r in range(n):
            table.append(list(input_data[ptr]))
            ptr += 1
        results.append(solve(table))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()