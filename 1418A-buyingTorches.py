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
        x = int(data[data_idx])
        data_idx += 1
        y = int(data[data_idx])
        data_idx += 1
        k = int(data[data_idx])
        data_idx += 1
        
        required_sticks = k * (y + 1) - 1
        a = (required_sticks + (x - 2)) // (x - 1)
        result = a + k
        output_lines.append(str(result))
        
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()