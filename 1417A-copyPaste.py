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
        k = int(data[data_idx])
        data_idx += 1
        
        a = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        min_val = a[0]
        
        for val in a:
            if val < min_val:
                min_val = val
        cnt = 0
        
        for val in a:
            if val != min_val:
                cnt += (k - val) // min_val
        
        output_lines.append(str(cnt))
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()