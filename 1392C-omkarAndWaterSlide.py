# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = list(map(int, sys.stdin.read().split()))

    if not data:
        return
    t = data[0]
    p = 1
    output = []

    for _ in range(t):
        n = data[p]
        p += 1
        prev = data[p]
        p += 1
        total = 0
        
        for _ in range(1, n):
            x = data[p]
            p += 1
            diff = prev - x

            if diff > 0:
                total += diff
            prev = x

        output.append(str(total))
    sys.stdout.write('\n'.join(output) + '\n')

alif()
