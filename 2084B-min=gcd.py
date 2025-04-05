# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        m = min(a)
        
        count_m = a.count(m)
        
        Q = []
        isMin = []
        for x in a:
            if x % m == 0:
                Q.append(x // m)
                isMin.append(x == m)
        
        dCount = len(Q)
        
        gAll = 0
        for i in range(dCount):
            gAll = Q[i] if i == 0 else gcd(gAll, Q[i])
        
        if gAll != 1:
            print("No")
            continue
            
        if dCount < 2:
            print("No")
            continue
            
        pre = [0] * dCount
        suf = [0] * dCount
        
        pre[0] = Q[0]
        for i in range(1, dCount):
            pre[i] = gcd(pre[i-1], Q[i])
            
        suf[dCount-1] = Q[dCount-1]
        for i in range(dCount-2, -1, -1):
            suf[i] = gcd(suf[i+1], Q[i])
            
        possible = False
        for i in range(dCount):
            if isMin[i]:
                gWithout = 0
                if i > 0:
                    gWithout = pre[i-1]
                if i < dCount-1:
                    gWithout = suf[i+1] if gWithout == 0 else gcd(gWithout, suf[i+1])
                    
                if gWithout == 1:
                    possible = True
                    break
        
        print("Yes" if possible else "No")

solve()