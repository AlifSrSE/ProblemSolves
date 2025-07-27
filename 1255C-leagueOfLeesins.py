# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1255/problem/C

import sys
import collections

def alif():
    n = int(sys.stdin.readline())
    v = collections.defaultdict(list)
    cnt = [0] * (n + 1)
    
    for _ in range(n - 2):
        x, y, z = map(int, sys.stdin.readline().split())
        v[x].append(y)
        v[x].append(z)
        v[y].append(x)
        v[y].append(z)
        v[z].append(x)
        v[z].append(y)
        cnt[x] += 1
        cnt[y] += 1
        cnt[z] += 1

    start_node = -1
    for p in range(1, n + 1):
        if cnt[p] == 1:
            start_node = p
            break
    
    first_neighbor_of_start = v[start_node][0]
    second_neighbor_of_start = v[start_node][1]

    current_node = start_node
    next_node = -1

    if cnt[first_neighbor_of_start] == 2:
        next_node = first_neighbor_of_start
    else:
        next_node = second_neighbor_of_start
    
    vis = [0] * (n + 1)
    result_permutation = []
    result_permutation.append(current_node)
    result_permutation.append(next_node)
    vis[current_node] = 1
    vis[next_node] = 1

    for _ in range(n - 2):
        found_z = -1

        for neighbor_of_current in v[current_node]:
            if vis[neighbor_of_current] == 0:
                found_z = neighbor_of_current
                break
        
        result_permutation.append(found_z)
        vis[found_z] = 1
        current_node = next_node
        next_node = found_z
    
    sys.stdout.write(" ".join(map(str, result_permutation)) + "\n")

if __name__ == "__main__":
    alif()