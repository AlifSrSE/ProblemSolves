# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from collections import defaultdict

def alif():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    data_idx = 0

    try:
        n = int(input_data[data_idx])
        data_idx += 1
    except IndexError:
        return

    cnt = defaultdict(int)
    two = 0
    four = 0
    six = 0
    eight = 0

    def update_counters_add(x):
        nonlocal two, four, six, eight
        cnt[x] += 1
        current_count = cnt[x]
        
        if current_count == 8:
            eight += 1
            six -= 1
        elif current_count == 6:
            six += 1
            four -= 1
        elif current_count == 4:
            four += 1
            two -= 1
        elif current_count == 2:
            two += 1

    def update_counters_remove(x):
        nonlocal two, four, six, eight
        
        if cnt[x] == 0:
             return
        
        old_count = cnt[x]
        cnt[x] -= 1
        new_count = cnt[x]

        if old_count == 8:
            eight -= 1
            six += 1
        elif old_count == 6:
            six -= 1
            four += 1
        elif old_count == 4:
            four -= 1
            two += 1
        elif old_count == 2:
            two -= 1

    for _ in range(n):
        x = int(input_data[data_idx])
        data_idx += 1
        update_counters_add(x)

    q = int(input_data[data_idx])
    data_idx += 1
    output = []
    
    for _ in range(q):
        w = input_data[data_idx]
        x = int(input_data[data_idx + 1])
        data_idx += 2
        
        if w == '+':
            update_counters_add(x)
        elif w == '-':
            update_counters_remove(x)

        is_possible = (
            eight > 0 or 
            (six > 0 and (four > 0 or two > 0)) or 
            (four > 0 and two > 1) or 
            (four > 1) or 
            (six > 1)
        )
        
        output.append("YES" if is_possible else "NO")

    sys.stdout.write('\n'.join(output) + '\n')

alif()
