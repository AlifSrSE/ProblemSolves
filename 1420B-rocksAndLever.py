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
        data_idx += 1
        
        v = [0] * 67
        res = 0
        
        for p in range(n):
            x = int(data[data_idx])
            data_idx += 1
            
            cnt = 0
            temp_x = x
            while temp_x > 1:
                temp_x //= 2
                cnt += 1
            
            res += v[cnt]
            v[cnt] += 1
            
        output.append(str(res))
    sys.stdout.write('\n'.join(output) + '\n')
alif()