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
        a = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n
        
        a.sort()
        prodA = a[n - 5] * a[n - 4] * a[n - 3] * a[n - 2] * a[n - 1]
        prodB = a[0] * a[1] * a[n - 3] * a[n - 2] * a[n - 1]
        prodC = a[0] * a[1] * a[2] * a[3] * a[n - 1]
        
        res = max(prodA, prodB, prodC)
        output_lines.append(str(res))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
