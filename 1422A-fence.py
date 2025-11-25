# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    data_idx = 1
    output = []
    for _ in range(t):
        a = int(data[data_idx])
        b = int(data[data_idx + 1])
        c = int(data[data_idx + 2])
        data_idx += 3
        result = a + b + c - 2
        output.append(str(result))
        
    sys.stdout.write('\n'.join(output) + '\n')
alif()