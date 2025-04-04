# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    s = input().strip()
    
    ans = int(s[0])
    for i in range(n-1):
        ans += s[i] != s[i + 1] 
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()