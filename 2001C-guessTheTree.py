# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def find_root(parents, node):
    if parents[node] == -1:
        return node
    parents[node] = find_root(parents, parents[node])
    return parents[node]

def main():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        parents = [-1] * n
        result = ["!"]
        
        for i in range(n):
            for j in range(i + 1, n):
                if find_root(parents, i) != find_root(parents, j):
                    v1, v2 = i, j
                    while True:
                        print(f"? {v1 + 1} {v2 + 1}", flush=True)
                        
                        x = int(input()) - 1
                        if x == v1:
                            result.extend([str(v1 + 1), str(v2 + 1)])
                            parents[find_root(parents, v2)] = find_root(parents, v1)
                            break
                            
                        if find_root(parents, x) != find_root(parents, v1):
                            v2 = x
                        else:
                            v1 = x
        
        print(' '.join(result), flush=True)

if __name__ == "__main__":
    main()