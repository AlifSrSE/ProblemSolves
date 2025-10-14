# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def solve():
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
        
        cnt = sum(a)
        
        if cnt <= n // 2:
            length = n // 2
            result = ["0"] * length
            output_lines.append(str(length))
            output_lines.append(" ".join(result))
        else:
            if cnt % 2 != 0:
                cnt -= 1
            
            length = cnt
            result = ["1"] * length
            output_lines.append(str(length))
            output_lines.append(" ".join(result))

    sys.stdout.write('\n'.join(output_lines) + '\n')

solve()
