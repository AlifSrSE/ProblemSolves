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
        s = data[data_idx]
        data_idx += 1
        x = int(data[data_idx])
        data_idx += 1
        n = len(s)
        w = list('1' * n)
        
        for p in range(n):
            if s[p] == '1':
                continue
            if p - x >= 0:
                w[p - x] = '0'
            if p + x < n:
                w[p + x] = '0'
        result = "".join(w)

        for p in range(n):
            if s[p] == '0':
                continue
            if p - x >= 0 and w[p - x] == '1':
                continue
            if p + x < n and w[p + x] == '1':
                continue
            
            result = "-1"
            break

        output_lines.append(result)
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
