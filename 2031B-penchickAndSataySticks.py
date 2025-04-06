# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    
    for _ in range(10):
        for i in range(n - 1):
            if p[i] == p[i + 1] + 1:
                p[i], p[i + 1] = p[i + 1], p[i]
    
    okay = all(p[i] == i for i in range(n))
    
    print("YES" if okay else "NO")

t = int(input())
for _ in range(t):
    solve()