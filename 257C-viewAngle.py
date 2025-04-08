# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def solve():
    PI = 4 * math.atan(1.0)
    n = int(input())
    phi = []
    
    for _ in range(n):
        x, y = map(float, input().split())
        phi.append(math.atan2(y, x) * 180.0 / PI)
    
    phi.sort()
    angle = 0.0
    for p in range(1, n):
        angle = max(angle, phi[p] - phi[p-1])
    
    angle = max(angle, 360.0 - (phi[-1] - phi[0]))
    print(f"{360.0 - angle:.8f}")

solve()