# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2004/problem/D
 
import sys
from collections import defaultdict

def has_same_color(type1, type2):
    return (type1[0] == type2[0] or type1[0] == type2[1] or
            type1[1] == type2[0] or type1[1] == type2[1])

def search(types, candidate_lists, target, node, rest):
    if rest == 0:
        return float('inf')

    if has_same_color(types[node], types[target]):
        return abs(node - target)

    result = float('inf')
    for candidate in candidate_lists[node]:
        distance = search(types, candidate_lists, target, candidate, rest - 1)
        if distance != float('inf'):
            result = min(result, abs(node - candidate) + distance)

    return result

def solve(types, x, y):
    candidate_lists = [[] for _ in range(len(types))]

    left_type_to_last_index = {}
    for i in range(len(types)):
        for left_type in left_type_to_last_index:
            if has_same_color(left_type, types[i]):
                candidate_lists[i].append(left_type_to_last_index[left_type])
        left_type_to_last_index[types[i]] = i

    right_type_to_last_index = {}
    for i in range(len(types) - 1, -1, -1):
        for right_type in right_type_to_last_index:
            if has_same_color(right_type, types[i]):
                candidate_lists[i].append(right_type_to_last_index[right_type])
        right_type_to_last_index[types[i]] = i

    results = []
    for i in range(len(x)):
        distance = search(types, candidate_lists, y[i] - 1, x[i] - 1, 4)
        results.append(str(-1 if distance == float('inf') else distance))

    return "\n".join(results)

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1

    for _ in range(t):
        n = int(input[idx])
        q = int(input[idx + 1])
        idx += 2

        types = input[idx:idx + n]
        idx += n

        x = []
        y = []
        for _ in range(q):
            x.append(int(input[idx]))
            y.append(int(input[idx + 1]))
            idx += 2

        print(solve(types, x, y))

if __name__ == "__main__":
    main()