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
        n = int(data[data_idx])
        x = int(data[data_idx + 1])
        data_idx += 2
        
        if n > 0:
            a = [int(data[data_idx + i]) for i in range(n)]
            data_idx += n
        else:
            a = []
            
        if not a:
            output.append("0")
            continue
            
        cnt = 0
        sum_diff = 0
        for val in a:
            if val == x:
                cnt += 1
            sum_diff += (val - x)
        
        if cnt == n:
            output.append("0")
        elif cnt > 0 or sum_diff == 0:
            output.append("1")
        else:
            output.append("2")
            
    sys.stdout.write('\n'.join(output) + '\n')
alif()