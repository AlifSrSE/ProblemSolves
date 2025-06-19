# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1218/problem/A

import sys
sys.setrecursionlimit(20000)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    edges = data[1:]
    
    from collections import defaultdict
    tree = defaultdict(list)
    
    # Build the adjacency list
    for i in range(0, len(edges), 2):
        u, v = int(edges[i]), int(edges[i+1])
        tree[u].append(v)
        tree[v].append(u)

    size = [0] * N
    dp = [0] * N  # dp[u] = sum of subtree sizes rooted at u
    ans = 0

    # First DFS: calculate sizes and dp[0]
    def dfs1(u, parent):
        size[u] = 1
        for v in tree[u]:
            if v != parent:
                dfs1(v, u)
                size[u] += size[v]
                dp[u] += dp[v]
        dp[u] += size[u]

    dfs1(0, -1)
    ans = dp[0]

    # Second DFS: re-rooting to calculate dp[u] for all u
    def dfs2(u, parent):
        nonlocal ans
        for v in tree[u]:
            if v != parent:
                # move root from u to v
                dp[v] = dp[u] - size[v] + (N - size[v])
                size_v_orig = size[v]
                size[v] = N  # when rerooted, v's size is total
                dfs2(v, u)
                size[v] = size_v_orig
                ans = max(ans, dp[v])

    dfs2(0, -1)
    print(ans)

if __name__ == "__main__":
    solve()