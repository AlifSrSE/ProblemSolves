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
        
        a = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n
        
        reversed_a = a[::-1]
        output_lines.append(" ".join(map(str, reversed_a)))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
