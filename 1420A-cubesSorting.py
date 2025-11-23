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
        
        if n == 0:
            output.append("YES")
            continue
            
        last = -1
        ans = False
        
        for p in range(n):
            x = int(data[data_idx])
            data_idx += 1
            if p > 0 and (x >= last):
                ans = True
            last = x
            
        output.append("YES" if ans else "NO")
    sys.stdout.write('\n'.join(output) + '\n')
alif()