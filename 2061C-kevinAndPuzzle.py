# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

MOD = 998244353

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    for i in range(n):
        a[i] = i - a[i]
    
    f = [0] * (n + 1)
    f[n] = 1
    
    for i in range(n - 1, -1, -1):
        if a[i] < 0:
            continue
        if i + 1 == n or (i + 1 < n and a[i + 1] == a[i] + 1):
            f[i] = (f[i] + f[i + 1]) % MOD
        if i + 2 == n or (i + 2 < n and a[i + 2] == a[i] + 1):
            f[i] = (f[i] + f[i + 2]) % MOD
    
    ans = 0
    if a[0] == 0:
        ans = (ans + f[0]) % MOD
    if n == 1 or (n > 1 and a[1] == 0):
        ans = (ans + f[1]) % MOD
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()