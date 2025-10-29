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
        a = int(data[data_idx])
        data_idx += 1
        b = int(data[data_idx])
        data_idx += 1
        diff = a - b

        if diff < 0:
            diff = -diff
        ans = (diff + 9) // 10
        output_lines.append(str(ans))

    sys.stdout.write('\n'.join(output_lines) + '\n')
alif()
