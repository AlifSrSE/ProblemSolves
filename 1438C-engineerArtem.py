#Author: AlifSrSE

import sys
from collections import defaultdict

def solve(a):
    n = len(a)
    m = len(a[0])
    value_to_points = defaultdict(list)
    for r in range(n):
        for c in range(m):
            value_to_points[a[r][c]].append((r, c))
    
    result = [[0] * m for _ in range(n)]
    count = 0
    for val in sorted(value_to_points.keys()):
        points = value_to_points[val]
        for r, c in points:
            result[r][c] = val + (0 if (r + c) % 2 == count % 2 else 1)
        count += 1
    
    return "\n".join(" ".join(map(str, row)) for row in result)

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
        a = []
        for r in range(n):
            a.append([int(x) for x in input_data[ptr : ptr+m]])
            ptr += m
        results.append(solve(a))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()