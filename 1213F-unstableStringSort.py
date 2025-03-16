# Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1213/problem/F
 
import sys
 
def read():
    return map(int, sys.stdin.readline().split())
 
def solve():
    n, m = read()
    P = list(read())
    Q = list(read())
    pos = [0] * (n + 1)
    L = [0] * (n + 1)
    bel = [0] * (n + 1)
    ans = [''] * (n + 1)
    
    for i in range(n):
        pos[P[i]] = i + 1
    
    k = n
    for i in range(n - 1, -1, -1):
        j = pos[Q[i]]
        k = min(k, j)
        L[j] = k
    
    j, k = 1, n
    for i in range(n, 0, -1):
        k = min(k, L[i])
        bel[i] = j
        if k == i:
            j += 1
    
    if bel[1] < m:
        print("NO")
        return
    
    print("YES")
    j = -1
    for i in range(1, n + 1):
        if bel[i] != bel[i - 1]:
            j += 1
        ans[P[i - 1]] = chr(ord('a') + min(25, j))
    
    print("".join(ans[1:]))
 
def main():
    solve()
 
if __name__ == "__main__":
    main()
