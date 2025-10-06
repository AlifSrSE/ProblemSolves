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
        s = data[data_idx]
        data_idx += 1
        
        pivot_char = s[n - 1]
        result = pivot_char * n
        output_lines.append(result)

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
