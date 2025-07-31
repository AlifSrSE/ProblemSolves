# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1264/A

import sys

def alif():
    t = int(sys.stdin.readline())
    while t:
        n = int(sys.stdin.readline())
        v = list(map(int, sys.stdin.readline().split()))
        v.append(v[-1] - 1) 
        d = []
        
        for p in range(1, n + 1):
            if v[p - 1] > v[p]:
                d.append(p)
                
                if p > (n // 2):
                    break
        g, s, b = 0, 0, 0
        
        if len(d) > 3:
            d.pop() 
            g = d[0]
            s = d[-1] - d[0]
            b = 0
            
            for p_idx in range(len(d) - 1, 0, -1):
                diff = d[p_idx] - d[p_idx - 1]
                
                if b <= g:
                    b += diff
                    s -= diff
                else:
                    break
            
            if g >= s or g >= b:
                g = s = b = 0
        
        sys.stdout.write(f"{g} {s} {b}\n")
        t -= 1

if __name__ == "__main__":
    alif()