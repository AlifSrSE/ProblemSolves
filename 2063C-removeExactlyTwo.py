# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2063/problem/C
 
def solve(u, v):
    n = len(u) + 1
    adj_sets = [set() for _ in range(n)]
    for i in range(len(u)):
        adj_sets[u[i] - 1].add(v[i] - 1)
        adj_sets[v[i] - 1].add(u[i] - 1)

    degree_to_count = {}
    for i in range(len(adj_sets)):
        update_map(degree_to_count, len(adj_sets[i]), 1)

    result = -1
    for i in range(n):
        involved = [i] + list(adj_sets[i])

        for node in involved:
            update_map(degree_to_count, len(adj_sets[node]), -1)

        for adj in adj_sets[i]:
            update_map(degree_to_count, len(adj_sets[adj]) - 1, 1)

        if not degree_to_count:
            max_degree = -1
        else:
            max_degree = max(degree_to_count.keys())

        result = max(result, len(adj_sets[i]) + (max_degree - 1 if max_degree != -1 else -1))

        for adj in adj_sets[i]:
            update_map(degree_to_count, len(adj_sets[adj]) - 1, -1)

        for node in involved:
            update_map(degree_to_count, len(adj_sets[node]), 1)

    return result

def update_map(degree_to_count, degree, delta):
    if degree != 0:
        degree_to_count[degree] = degree_to_count.get(degree, 0) + delta
        if degree_to_count[degree] == 0:
            if degree in degree_to_count:
                del degree_to_count[degree]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        u = []
        v = []
        for _ in range(n - 1):
            ui, vi = map(int, input().split())
            u.append(ui)
            v.append(vi)

        print(solve(u, v))