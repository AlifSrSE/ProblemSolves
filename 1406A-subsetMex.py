# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from collections import Counter

def alif():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    data_idx = 0
    t = int(input_data[data_idx])
    data_idx += 1
    
    output_lines = []
    MAX_CHECK = 102 

    for _ in range(t):
        if data_idx >= len(input_data):
            break
            
        n = int(input_data[data_idx])
        data_idx += 1
        a = [int(x) for x in input_data[data_idx:data_idx + n]]
        data_idx += n
        counts = Counter(a)
        
        s = 0
        empty = True
        
        for p in range(MAX_CHECK):
            count_p = counts.get(p, 0)
            
            if count_p >= 2:
                continue
                
            elif count_p == 1:
                if empty:
                    s = p
                    empty = False
                
            elif count_p == 0:
                
                if empty:
                    s += 2 * p
                else:
                    s += p
                break 
        
        output_lines.append(str(s))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
