# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))  
    
    pos = 0
    neg = 0
    totPos = 0
    totNeg = 0
    
    for x in a:
        if x > 0:
            totPos += abs(x)
        else:
            totNeg += abs(x)
    
    ans = max(totPos, totNeg)
    
    for x in a:
        if x > 0:
            pos += abs(x)
        else:
            neg += abs(x)
        ans = max(ans, pos + totNeg - neg)
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()