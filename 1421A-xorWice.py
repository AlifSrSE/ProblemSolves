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
        data_idx += 2
        output.append(str(a ^ b))
    sys.stdout.write('\n'.join(output) + '\n')
alif()