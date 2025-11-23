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
        q = int(data[data_idx + 1])
        data_idx += 2
        
        if n == 0:
            output.append("0")
            continue
            
        a = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        f = a[0]
        g = 0
        
        for p in range(1, n):
            new_f = max(f, g + a[p])
            new_g = max(g, f - a[p])
            
            f = new_f
            g = new_g
            
        output.append(str(max(f, g)))
    sys.stdout.write('\n'.join(output) + '\n')
alif()