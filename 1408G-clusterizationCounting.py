# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    MOD = 998244353
    n = int(sys.stdin.readline())
    adj = []

    for _ in range(n):
        adj.append(list(map(int, sys.stdin.readline().split())))
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((adj[i][j], i, j))
    edges.sort()
    parent = list(range(n))

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
            return root_i, root_j, root_j
        return None, None, root_i
    
    size = [1] * n
    edges_count = [0] * n
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(n):
        dp[i][1] = 1

    def convolve(dp1, dp2, n_limit):
        size1 = next((i for i, x in enumerate(dp1) if x != 0), 0)
        size1 = len(dp1) - size1
        
        size2 = next((i for i, x in enumerate(dp2) if x != 0), 0)
        size2 = len(dp2) - size2
        
        max_k = 0
        for i in range(1, n_limit + 1):
            if dp1[i] != 0:
                max_k += i
                break
        for i in range(1, n_limit + 1):
            if dp2[i] != 0:
                max_k += i
                break

        max_k = min(n_limit, sum(i * (1 if d[i] != 0 else 0) for i, d in enumerate([dp1, dp2])))

        new_dp = [0] * (n_limit + 1)
        for i in range(1, n_limit + 1):
            if dp1[i] == 0:
                continue
            for j in range(1, n_limit + 1):
                if dp2[j] == 0:
                    continue
                if i + j <= n_limit:
                    term = (dp1[i] * dp2[j]) % MOD
                    new_dp[i + j] = (new_dp[i + j] + term) % MOD
        
        return new_dp

    for _, u, v in edges:
        r_u = find(u)
        r_v = find(v)

        if r_u != r_v:
            s_u = size[r_u]
            s_v = size[r_v]
            e_u = edges_count[r_u]
            e_v = edges_count[r_v]
            
            if s_u > s_v:
                r_u, r_v = r_v, r_u
            parent[r_u] = r_v
            r_new = r_v

            s_new = s_u + s_v
            e_new = e_u + e_v + 1
            size[r_new] = s_new
            edges_count[r_new] = e_new
            dp_new = convolve(dp[r_u], dp[r_v], n)
            
            if e_new == s_new - 1:
                dp_new[1] = (dp_new[1] + 1) % MOD
            dp[r_new] = dp_new
            
        else:
            edges_count[r_u] += 1
            
    final_root = find(0)
    print(*(dp[final_root][1:]))

alif()