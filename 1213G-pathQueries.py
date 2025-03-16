# Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1213/problem/G
 
import sys
 
class DSU:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [1] * n
        self.res = 0
    
    def find(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def merge(self, u, v):
        u = self.find(u)
        v = self.find(v)
        
        if u == v:
            return
        
        if self.rank[u] < self.rank[v]:
            u, v = v, u
        
        self.res -= self.get(self.rank[u])
        self.res -= self.get(self.rank[v])
        self.res += self.get(self.rank[u] + self.rank[v])
        
        self.rank[u] += self.rank[v]
        self.parent[v] = u
    
    def get(self, cnt):
        return cnt * (cnt - 1) // 2
 
def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    dsu = DSU(n)
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u - 1, v - 1))
    
    queries = []
    for i, x in enumerate(map(int, sys.stdin.readline().split())):
        queries.append((x, i))
    
    edges.sort()
    queries.sort()
    
    ans = [0] * m
    index = 0
    
    for q, i in queries:
        while index < len(edges) and edges[index][0] <= q:
            _, u, v = edges[index]
            dsu.merge(u, v)
            index += 1
        ans[i] = dsu.res
    
    print(" ".join(map(str, ans)))
 
def main():
    solve()
 
if __name__ == "__main__":
    main()
