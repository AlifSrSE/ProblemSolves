def search(leaf_nums, adj_lists, node, parent):
    for adj in adj_lists[node]:
        if adj != parent:
            search(leaf_nums, adj_lists, adj, node)
            leaf_nums[node] += leaf_nums[adj]
    
    leaf_nums[node] = max(1, leaf_nums[node])

def solve(u, v, x, y):
    n = len(u) + 1
    
    adj_lists = [[] for _ in range(n)]
    for i in range(len(u)):
        adj_lists[u[i]].append(v[i])
        adj_lists[v[i]].append(u[i])
    
    leaf_nums = [0] * n
    search(leaf_nums, adj_lists, 0, -1)
    
    results = [str(leaf_nums[x[i]] * leaf_nums[y[i]]) for i in range(len(x))]
    return "\n".join(results)

t = int(input())
for _ in range(t):
    n = int(input())
    u = []
    v = []
    for _ in range(n-1):
        ui, vi = map(int, input().split())
        u.append(ui - 1)
        v.append(vi - 1)
    
    q = int(input())
    x = []
    y = []
    for _ in range(q):
        xi, yi = map(int, input().split())
        x.append(xi - 1)
        y.append(yi - 1)
    
    print(solve(u, v, x, y))