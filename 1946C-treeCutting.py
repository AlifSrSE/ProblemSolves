# Author: AlifSrSe
# date: 2025-03-22
# https://codeforces.com/problemset/problem/1946/C
 
def solve():
    n, k = map(int, input().split())
    v = []
    u = []
    for _ in range(n - 1):
        vi, ui = map(int, input().split())
        v.append(vi)
        u.append(ui)

    adj_lists = [[] for _ in range(n)]
    for i in range(n - 1):
        adj_lists[v[i] - 1].append(u[i] - 1)
        adj_lists[u[i] - 1].append(v[i] - 1)

    result = -1
    lower = 1
    upper = n
    while lower <= upper:
        middle = (lower + upper) // 2
        if check(k, adj_lists, middle):
            result = middle
            lower = middle + 1
        else:
            upper = middle - 1

    return result

def check(k, adj_lists, min_size):
    return search(k, adj_lists, min_size, -1, 0)[0] >= k + 1

def search(k, adj_lists, min_size, parent, node):
    component_count = 0
    size = 1
    for adj in adj_lists[node]:
        if adj != parent:
            outcome = search(k, adj_lists, min_size, node, adj)
            component_count += outcome[0]
            size += outcome[1]

    if size >= min_size:
        component_count += 1
        size = 0

    return (component_count, size)

t = int(input())
for _ in range(t):
    print(solve())