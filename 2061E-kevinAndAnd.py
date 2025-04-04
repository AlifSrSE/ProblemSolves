# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

ALL = (1 << 30) - 1

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = sum(a) 
    b = [x ^ ALL for x in b]
    
    cand = [0] * (1 << m)
    pop = [0] * (1 << m)
    for mask in range(1 << m):
        here = 0
        for i in range(m):
            if mask & (1 << i):
                here |= b[i]
        cand[mask] = ALL ^ here
        pop[mask] = bin(mask).count('1') 
    
    out = []
    for i in range(n):
        best = [a[i]] * (m + 1)
        for mask in range(1 << m):
            here = a[i] & cand[mask]
            best[pop[mask]] = min(best[pop[mask]], here)
        
        for j in range(m, 0, -1):
            out.append(best[j - 1] - best[j])
    
    out.sort(reverse=True)
    
    ans -= sum(out[:k])
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()