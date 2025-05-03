# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1167/problem/C

def find_root(parents, node):
    root = node
    while parents[root] != -1:
        root = parents[root]
    
    p = node
    while p != root:
        next_p = parents[p]
        parents[p] = root
        p = next_p
    
    return root

def alif(n, groups):
    parents = [-1] * n
    
    for group in groups:
        for i in range(len(group) - 1):
            root1 = find_root(parents, group[i])
            root2 = find_root(parents, group[i + 1])
            if root1 != root2:
                parents[root2] = root1
    
    root_to_size = {}
    for i in range(n):
        root = find_root(parents, i)
        root_to_size[root] = root_to_size.get(root, 0) + 1
    
    return ' '.join(str(root_to_size[find_root(parents, i)]) for i in range(n))

n, m = map(int, input().split())
groups = []
for _ in range(m):
    k, *group = map(int, input().split())
    groups.append([x - 1 for x in group])
print(alif(n, groups))