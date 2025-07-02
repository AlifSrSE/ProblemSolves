# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1244/problem/D

import sys
import collections
import itertools

def alif():
    n = int(sys.stdin.readline())
    cost = [[0] * (n + 1) for _ in range(4)]

    for row_idx in range(1, 4):
        node_costs = list(map(int, sys.stdin.readline().split()))
        for p in range(n):
            cost[row_idx][p + 1] = node_costs[p]
    g = collections.defaultdict(list)
    degree = [0] * (n + 1)
    possible = True

    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        g[x].append(y)
        g[y].append(x)
        degree[x] += 1
        degree[y] += 1

        if degree[x] > 2 or degree[y] > 2:
            possible = False

    if not possible:
        sys.stdout.write("-1\n")
        return
    start_node = -1

    for p in range(1, n + 1):
        if degree[p] == 1:
            start_node = p
            break

    if n == 1:
        start_node = 1
    
    v_path_pos = [0] * (n + 1)
    current_node = start_node
    previous_node = 0
    
    for count in range(1, n + 1):
        v_path_pos[current_node] = count
        next_node = -1

        for neighbor in g[current_node]:
            if neighbor != previous_node:
                next_node = neighbor
                break
        
        previous_node = current_node
        current_node = next_node

    base_colors = [1, 2, 3]
    min_total_cost = float('inf')
    best_scheme = []

    for current_perm in itertools.permutations(base_colors):
        current_total_cost = 0
        
        for node_id in range(1, n + 1):
            path_position = v_path_pos[node_id]
            color_to_assign = current_perm[(path_position - 1) % 3]
            current_total_cost += cost[color_to_assign][node_id]
        
        if current_total_cost < min_total_cost:
            min_total_cost = current_total_cost
            best_scheme = list(current_perm)
            
    sys.stdout.write(f"{min_total_cost}\n")
    result_colors = [0] * (n + 1)

    for node_id in range(1, n + 1):
        path_position = v_path_pos[node_id]
        assigned_color = best_scheme[(path_position - 1) % 3]
        result_colors[node_id] = assigned_color
    sys.stdout.write(" ".join(map(str, result_colors[1:])) + "\n")

if __name__ == "__main__":
    alif()