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
        
        a = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n
        b = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n
        c = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n

        p = [0] * n
        
        p[0] = a[0]
        prev = p[0]
        
        for i in range(1, n - 1):
            if a[i] != prev:
                cur = a[i]
            elif b[i] != prev:
                cur = b[i]
            else:
                cur = c[i]
                
            p[i] = cur
            prev = cur
        
        p_prev = p[n - 2]
        p_first = p[0]
        
        if a[n - 1] != p_prev and a[n - 1] != p_first:
            cur = a[n - 1]
        elif b[n - 1] != p_prev and b[n - 1] != p_first:
            cur = b[n - 1]
        else:
            cur = c[n - 1]
            
        p[n - 1] = cur
        
        output_lines.append(" ".join(map(str, p)))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
