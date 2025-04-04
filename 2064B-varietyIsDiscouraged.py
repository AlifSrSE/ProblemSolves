# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(n):
        a[i] -= 1  
        c[a[i]] += 1
    
    for i in range(n):
        a[i] = 1 if c[a[i]] == 1 else 0
    
    best = 0
    L = -1
    R = -1
    
    i = 0
    while i < n:
        if a[i]:
            j = i
            while j < n and a[j]:
                j += 1
            if j - i > best:
                best = j - i
                L = i + 1
                R = j
            i = j
        else:
            i += 1
    
    if L == -1:
        print(0)
    else:
        print(L, R)

t = int(input())
for _ in range(t):
    solve()