# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = sys.stdin.read().split()

    if not data:
        return
    t = int(data[0])
    pointer = 1
    output = []

    for _ in range(t):
        l = int(data[pointer])
        r = int(data[pointer + 1])
        pointer += 2
        
        if 2 * l > r:
            output.append("-1 -1")
        else:
            output.append(f"{l} {2 * l}")
    sys.stdout.write('\n'.join(output) + '\n')

alif()