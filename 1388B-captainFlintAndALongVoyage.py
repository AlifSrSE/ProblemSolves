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
        n = int(data[pointer])
        pointer += 1
        g = (n + 3) // 4
        result = ""

        for p in range(g, n):
            result += "9"
        
        for p in range(g):
            result += "8"
        
        output.append(result)
    sys.stdout.write('\n'.join(output) + '\n')

alif()
