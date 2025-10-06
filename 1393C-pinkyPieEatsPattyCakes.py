# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from collections import Counter

def alif():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    data_idx = 0
    t = int(input_data[data_idx])
    data_idx += 1
    output = []
    
    for _ in range(t):
        n = int(input_data[data_idx])
        data_idx += 1
        elements = [int(input_data[i]) for i in range(data_idx, data_idx + n)]
        data_idx += n
        cnt = Counter(elements)
        mx = 0
        rep = 0
        
        for count in cnt.values():
            if count > mx:
                mx = count
                rep = 1
            elif count == mx:
                rep += 1

        if mx == 1:
            ans = n - 1
        else:
            ans = (n - rep) // (mx - 1) - 1
        
        output.append(str(ans))

    sys.stdout.write('\n'.join(output) + '\n')

alif()
