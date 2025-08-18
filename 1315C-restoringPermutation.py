# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1315/problem/C

def alif():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        a = [0] * (2 * n)
        used = [False] * (2 * n + 1)
        possible = True
        
        for i in range(n):
            val = b[i]
            if used[val]:
                possible = False
                break
            a[2 * i] = val
            used[val] = True
            
        if not possible:
            print(-1)
            continue
            
        for i in range(n):
            val_b = a[2 * i]
            found = False
            for j in range(val_b + 1, 2 * n + 1):
                if not used[j]:
                    a[2 * i + 1] = j
                    used[j] = True
                    found = True
                    break
            
            if not found:
                possible = False
                break
        
        if possible:
            print(*a)
        else:
            print(-1)

alif()