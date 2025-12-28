#Author: AlifSrSE

import sys

def find_root(parents, node):
    root = node
    while parents[root] != -1:
        root = parents[root]
    
    p = node
    while p != root:
        next_node = parents[p]
        parents[p] = root
        p = next_node
    return root

def solve(a):
    n = len(a)
    parents = [-1] * n
    roads = []
    for x in range(n):
        for y in range(x + 1, n):
            root_x = find_root(parents, x)
            root_y = find_root(parents, y)
            if a[x] != a[y] and root_x != root_y:
                parents[root_y] = root_x
                roads.append(f"{x + 1} {y + 1}")
    
    if len(roads) == n - 1:
        return f"YES\n" + "\n".join(roads)
    else:
        return "NO"

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        a = [int(x) for x in input_data[ptr + 1 : ptr + 1 + n]]
        results.append(solve(a))
        ptr += 1 + n
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
    