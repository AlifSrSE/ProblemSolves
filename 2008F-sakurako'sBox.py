# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2008/problem/F

MOD = 10**9 + 7
N = 200010

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    s = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        s[i + 1] = (s[i + 2] + a[i]) % MOD
        
    ans = 0
    for i in range(n - 1):
        ans = (ans + 2 * a[i] * s[i + 2] * inv[n] * inv[n - 1]) % MOD
    
    print(ans)

inv = [0] * N
inv[0] = inv[1] = 1
for i in range(2, N):
    inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD

t = int(input())
for _ in range(t):
    solve()