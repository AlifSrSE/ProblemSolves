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
        a = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        pos = {}

        for p in range(n):
            x = a[p]
            if x not in pos:
                pos[x] = []
            pos[x].append(p)
            
        idx = n + 1
        res = [-1] * (n + 1)
        
        for num in sorted(pos.keys()):
            cur = pos[num]
            cur.append(n)
            prev = -1
            mx = 0
            
            for p in range(len(cur)):
                dist = cur[p] - prev
                if dist > mx:
                    mx = dist
                prev = cur[p]
            
            start_k = mx
            end_k = idx
            
            for p in range(start_k, end_k):
                res[p] = num
            
            if mx < idx:
                idx = mx

        output_lines.append(" ".join(map(str, res[1:])))
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()