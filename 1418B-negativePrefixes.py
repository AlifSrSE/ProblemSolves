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
        v = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        locked = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        unlocked_values = []
        
        for p in range(n):
            if not locked[p]:
                unlocked_values.append(v[p])
        
        unlocked_values.sort(reverse=True)
        result = []
        unlocked_idx = 0
        
        for p in range(n):
            if locked[p]:
                result.append(v[p])
            else:
                result.append(unlocked_values[unlocked_idx])
                unlocked_idx += 1

        output_lines.append(" ".join(map(str, result)))
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()