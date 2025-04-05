# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    
    if n % 2 == 0:
        print(-1)
    else:
        perm = [n, 1] + [i-1 for i in range(3, n+1)]
        print(" ".join(map(str, perm)))

t = int(input())
for _ in range(t):
    solve()