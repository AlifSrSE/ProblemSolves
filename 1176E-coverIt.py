# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/1176/problem/E

from collections import deque

def alif(n, v, u):
    adj_sets = [set() for _ in range(n)]
    for i in range(len(v)):
        adj_sets[v[i] - 1].add(u[i] - 1)
        adj_sets[u[i] - 1].add(v[i] - 1)

    one_degree_nodes = deque()
    for i in range(n):
        if len(adj_sets[i]) == 1:
            one_degree_nodes.append(i)

    chosen = []
    removed = [False] * n
    index = 0
    while True:
        while index < n and removed[index]:
            index += 1
        if index == n:
            break

        while one_degree_nodes and (removed[one_degree_nodes[0]] or len(adj_sets[one_degree_nodes[0]]) != 1):
            one_degree_nodes.popleft()

        if not one_degree_nodes:
            chosen.append(index)
            remove(adj_sets, one_degree_nodes, removed, index)
            adj = next(iter(adj_sets[index]))
            remove(adj_sets, one_degree_nodes, removed, adj)
        else:
            node = next(iter(adj_sets[one_degree_nodes.popleft()]))
            chosen.append(node)
            remove(adj_sets, one_degree_nodes, removed, node)

    chosen_nodes = [node + 1 for node in chosen]
    return f"{len(chosen)}\n{' '.join(map(str, chosen_nodes))}"

def remove(adj_sets, one_degree_nodes, removed, node):
    for adj in list(adj_sets[node]):
        adj_sets[adj].remove(node)
        if not adj_sets[adj]:
            removed[adj] = True
        elif len(adj_sets[adj]) == 1:
            one_degree_nodes.append(adj)
    removed[node] = True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        v = []
        u = []
        for _ in range(m):
            vi, ui = map(int, input().split())
            v.append(vi)
            u.append(ui)
        print(alif(n, v, u))
