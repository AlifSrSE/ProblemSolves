# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    data_idx = 1
    output = []
    for _ in range(t):
        n = int(data[data_idx])
        s = data[data_idx + 1]
        data_idx += 2
        turn = (n % 2 == 0)
        win = False
        start_index = 1 if turn else 0
        target_parity = 0 if turn else 1
        for p in range(start_index, n, 2):
            digit = int(s[p])
            if digit % 2 == target_parity:
                win = True
                break
        result = 2 - (int(turn) ^ int(win))
        output.append(str(result))
    sys.stdout.write('\n'.join(output) + '\n')
alif()