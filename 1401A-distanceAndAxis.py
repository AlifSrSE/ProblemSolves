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
        k = int(data[data_idx])
        data_idx += 1
        res = k - n if k > n else (n - k) % 2
        output_lines.append(str(res))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
