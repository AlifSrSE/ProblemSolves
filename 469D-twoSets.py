def divide_sets(n, a, b, p):
    index_map = {p[i]: i for i in range(n)}
    assignment = [-1] * n 
 
    for i in range(n):
        if assignment[i] == -1:
            x = p[i]
            if (a - x) in index_map and assignment[index_map[a - x]] == -1:
                assignment[i] = 0
                assignment[index_map[a - x]] = 0
            elif (b - x) in index_map and assignment[index_map[b - x]] == -1:
                assignment[i] = 1
                assignment[index_map[b - x]] = 1
            else:
                print("NO")
                return
 
    print("YES")
    print(" ".join(map(str, assignment)))
 
 
n, a, b = map(int, input().split())
p = list(map(int, input().split()))
 
divide_sets(n, a, b, p)