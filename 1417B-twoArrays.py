# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

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
        u = int(data[data_idx])
        data_idx += 1
        
        a = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        q = 0
        result = []
        
        for x in a:
            if 2 * x < u:
                result.append("0")
            elif 2 * x > u:
                result.append("1")
            elif 2 * x == u:
                result.append(str(q))
                q = 1 - q
                
        output_lines.append(" ".join(result)) 
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()