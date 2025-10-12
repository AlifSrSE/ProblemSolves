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
        
        avail = 0
        cnt = 0
        
        for x_val in a:
            x = x_val
            if x > 0:
                avail += x
            elif x < 0:
                if x + avail > 0:
                    avail += x
                else:
                    x += avail
                    cnt -= x
                    avail = 0
        
        output_lines.append(str(cnt))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
