# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
import heapq

def alif():
    sys.setrecursionlimit(200000)
    input = sys.stdin.read
    data = input().split()

    m = int(data[0])
    n = int(data[1])
    a = [0] * m
    b = [0] * n
    current_index = 2

    for i in range(m):
        a[i] = int(data[current_index])
        current_index += 1
        
    for i in range(n):
        b[i] = int(data[current_index])
        current_index += 1
    sets = []

    for i in range(m):
        s_i = int(data[current_index])
        current_index += 1
        elements = []
        for _ in range(s_i):
            elements.append(int(data[current_index]) - 1)
            current_index += 1
        sets.append(elements)
    edges = []
    total_benefit = 0
    
    for i in range(m):
        set_node = n + i
        a_i = a[i]
        
        for element_node in sets[i]:
            b_j = b[element_node]
            weight = a_i + b_j
            total_benefit += weight
            heapq.heappush(edges, (-weight, element_node, set_node))
    parent = list(range(n + m))

    def find(i):
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    max_spanning_forest_weight = 0
    
    while edges:
        neg_weight, u, v = heapq.heappop(edges)
        weight = -neg_weight
        
        if union(u, v):
            max_spanning_forest_weight += weight
    min_cost = total_benefit - max_spanning_forest_weight
    
    print(min_cost)

alif()