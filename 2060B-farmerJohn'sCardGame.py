# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2060/problem/B

def solve():
    n, m = map(int, input().split())
    ara = []
    for _ in range(n):
        row = list(map(int, input().split()))
        row.sort()
        ara.append(row)

    vect = []
    for i in range(n):
        vect.append((ara[i][0], i))
    
    vect.sort()

    p = 0
    for i in range(n):
        if vect[i][0] != i:
            p = 1
            break
    
    if p == 1:
        print("-1")
        return
    
    for j in range(1, m):
        for i in range(n):
            if ara[vect[i][1]][j] != j * n + i:
                p = 1
                break
        if p == 1:
            break
    
    if p == 1:
        print("-1")
    else:
        result = [v[1] + 1 for v in vect]
        print(*result)

t = int(input())
for _ in range(t):
    solve()