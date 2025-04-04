# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(p, u, k):
    n = len(p) + 1
    child_lists = [[] for _ in range(n)]
    for i, parent in enumerate(p):
        child_lists[parent - 1].append(i + 1)
    for child_list in child_lists:
        child_list.sort()

    sequence = []
    subtree_sizes = [0] * n
    stack = [(0, False)] 
    
    while stack:
        node, processed = stack.pop()
        if not processed:
            sequence.append(node)
            stack.append((node, True)) 
            for child in reversed(child_lists[node]): 
                stack.append((child, False))
        else:
            subtree_sizes[node] = 1
            for child in child_lists[node]:
                subtree_sizes[node] += subtree_sizes[child]

    node_to_index = {node: index for index, node in enumerate(sequence)}

    result = []
    for i in range(len(u)):
        if k[i] <= subtree_sizes[u[i] - 1]:
            result.append(sequence[node_to_index[u[i] - 1] + k[i] - 1] + 1)
        else:
            result.append(-1)

    return "\n".join(map(str, result))

def main():
    n, q = map(int, input().split())
    p = list(map(int, input().split()))
    u = []
    k = []
    for _ in range(q):
        ui, ki = map(int, input().split())
        u.append(ui)
        k.append(ki)
    print(solve(p, u, k))

if __name__ == "__main__":
    main()