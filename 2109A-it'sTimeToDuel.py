# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2109/problem/A

from collections import deque

def alif(n, a):
    m = n - 1
    aImp = [[] for _ in range(m + 1)]
    units = []

    for i in range(1, n + 1):
        if a[i - 1] == 0:
            if i > 1:
                units.append((i - 1, True))
            if i < n:
                units.append((i, False))
        else:
            if i == 1:
                units.append((1, True))
            elif i == n:
                units.append((n - 1, False))
            else:
                aImp[i - 1].append(i)

    asgn = [-1] * (m + 1)
    dequ = deque(units)
    bad = False
    
    while dequ and not bad:
        v, val = dequ.popleft()
        if asgn[v] != -1:
            if asgn[v] != (1 if val else 0):
                bad = True
            continue
        asgn[v] = 1 if val else 0
        if val:
            for to in aImp[v]:
                dequ.append((to, True))
    
    return bad

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if alif(n, a) else "NO")