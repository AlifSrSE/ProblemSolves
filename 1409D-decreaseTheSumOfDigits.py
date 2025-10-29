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
        num = data[data_idx]
        data_idx += 1
        s = int(data[data_idx])
        data_idx += 1

        digits = list(map(int, num))
        total = sum(digits)

        if total <= s:
            output_lines.append("0")
            continue

        mult = 1
        cnt = 0

        for i in range(len(digits)-1, -1, -1):
            if total <= s:
                break
            total -= digits[i]
            add = (10 - digits[i]) % 10
            cnt += add * mult
            mult *= 10
            total += 1

        output_lines.append(str(cnt))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
