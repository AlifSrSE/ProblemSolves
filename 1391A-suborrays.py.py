# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = sys.stdin.read().split()
    t = int(data[0])
    pointer = 1
    output = []

    for _ in range(t):
        n = int(data[pointer])
        pointer += 1
        
        result = " ".join(map(str, range(1, n + 1)))
        output.append(result)

    sys.stdout.write('\n'.join(output) + '\n')

alif()
