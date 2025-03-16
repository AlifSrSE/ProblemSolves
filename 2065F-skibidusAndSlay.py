# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/F
 
import sys
 
input = sys.stdin.readline
print = sys.stdout.write
 
def solve():
    m = int(input())
    b = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(m + 1)]
    for _ in range(m - 1):
        f, g = map(int, input().split())
        adj[f].append(g)
        adj[g].append(f)
    
    h = ['0'] * (m + 1)
    
    for i in range(1, m + 1):
        for j in adj[i]:
            if i < j and b[i] == b[j]:
                h[b[i]] = '1'
    
    for i in range(1, m + 1):
        if len(adj[i]) < 2:
            continue
        v = [b[it] for it in adj[i]]
        v.sort()
        
        n = 1
        for j in range(1, len(v)):
            if v[j] == v[j - 1]:
                n += 1
            else:
                if n >= 2:
                    h[v[j - 1]] = '1'
                n = 1
        if n >= 2:
            h[v[-1]] = '1'
    
    ans = "".join(h[1:])
    print(ans + "\n")
 
t = int(input())
for _ in range(t):
    solve()