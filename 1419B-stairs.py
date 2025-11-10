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
        x = int(data[data_idx])
        data_idx += 1
        y = 1
        res = 0
        while x * 2 >= y * (y + 1):
            cost = y * (y + 1) // 2
            x -= cost
            y = 2 * y + 1
            res += 1
        output.append(str(res))
    sys.stdout.write('\n'.join(output) + '\n')
alif()