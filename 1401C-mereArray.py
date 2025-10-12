# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
import math

def alif():
    data = sys.stdin.read().split()
    
    if not data:
        return

    data_idx = 0
    t = int(data[data_idx])
    data_idx += 1
    
    output_lines = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        
        a = []
        for i in range(n):
            a.append(int(data[data_idx]))
            data_idx += 1
            
        mn = min(a)
        b = sorted(a)
        
        possible = True
        for i in range(n):
            if a[i] != b[i] and a[i] % mn != 0:
                possible = False
                break
        
        output_lines.append("YES" if possible else "NO")

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
