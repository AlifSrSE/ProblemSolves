# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve():
    t = int(sys.stdin.readline().strip())
    
    for _ in range(t):
        n, k, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        T = sum(a)
        
        P = [0] * (n + 1)
        for i in range(1, n + 1):
            P[i] = P[i - 1] + a[i - 1]
        
        X_val = k * T - x
        ans = 0
        
        if X_val < 0:
            print(0)
            continue
        
        for r in range(n):
            if P[r] > X_val:
                continue
            max_p = (X_val - P[r]) // T
            count_p = min(k, max_p + 1)
            ans += count_p
        
        print(ans)

if __name__ == "__main__":
    solve()