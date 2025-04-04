# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve():
    LG = 30
    
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, q = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        a.reverse()
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] ^ a[i - 1]
        
        f = [{bit: {} for bit in range(LG)} for _ in range(2)]
        
        for i in range(1, n + 1):
            A = prefix[i - 1]
            B = a[i - 1]
            x = A ^ B
            
            for bit in range(LG):
                x &= ~(1 << bit)
                if (B >> bit) & 1:
                    where = f[(A >> bit) & 1][bit]
                    if x not in where:
                        where[x] = i
                    else:
                        where[x] = min(where[x], i)
        
        result = []
        for _ in range(q):
            x = int(sys.stdin.readline().strip())
            ans = n + 1
            
            for bit in range(LG):
                here = (x >> bit) & 1
                x &= ~(1 << bit)
                where = f[here][bit]
                if x in where:
                    ans = min(ans, where[x])
            
            result.append(str(ans - 1))
        
        print(" ".join(result))

if __name__ == "__main__":
    solve()