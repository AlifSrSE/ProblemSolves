# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    INF = float('inf')
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
        
        if n == 0:
            a = []
        else:
            a = [int(data[data_idx + i]) for i in range(n)]
            data_idx += n

        if n == 0:
            output_lines.append("0")
            continue
        
        f = [INF] * n
        g = [INF] * n
        g[0] = a[0]

        if n > 1:
            g[1] = a[0] + a[1]
            f[1] = g[0]

        for p in range(2, n):
            f[p] = min(g[p - 1], g[p - 2])
            cost_clear_1 = f[p - 1] + a[p]
            cost_clear_2 = f[p - 2] + a[p - 1] + a[p]
            
            g[p] = min(cost_clear_1, cost_clear_2)
        
        result = min(f[n - 1], g[n - 1])
        output_lines.append(str(result))
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()