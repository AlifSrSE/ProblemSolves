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
        k = int(data[data_idx])
        data_idx += 1
        s = set()

        for _ in range(n):
            s.add(int(data[data_idx]))
            data_idx += 1
        
        unique_count = len(s)
        
        if k == 1:
            ans = 1 if unique_count <= 1 else -1
            
        else:
            if unique_count <= k:
                ans = 1
            else:
                ans = (unique_count - 1 + k - 2) // (k - 1)
                ans = max(1, ans)

        output_lines.append(str(ans))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
