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
        x0 = int(data[data_idx])
        x1 = int(data[data_idx + 1])
        x2 = int(data[data_idx + 2])
        data_idx += 3
        
        y0 = int(data[data_idx])
        y1 = int(data[data_idx + 1])
        y2 = int(data[data_idx + 2])
        data_idx += 3

        res = 0
        
        # 1. Maximize +2 pairings (x2 vs y1)
        q = min(x2, y1)
        res += 2 * q
        x2 -= q
        y1 -= q
        
        # 2. Use remaining x2 (score 0)
        q = min(x2, y2)
        x2 -= q
        y2 -= q
        
        q = min(x2, y0)
        x2 -= q
        y0 -= q
        
        # 3. Use remaining x0 (score 0)
        q = min(x0, y2)
        x0 -= q
        y2 -= q
        
        q = min(x0, y0)
        x0 -= q
        y0 -= q
        
        q = min(x0, y1)
        x0 -= q
        y1 -= q
        
        # 4. Use x1, prioritizing 0 score
        q = min(x1, y0)
        x1 -= q
        y0 -= q
        
        q = min(x1, y1)
        x1 -= q
        y1 -= q
        
        # 5. Calculate -2 penalty (remaining x1 vs y2)
        q = min(x1, y2)
        res -= 2 * q
        x1 -= q
        y2 -= q

        output_lines.append(str(res))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()