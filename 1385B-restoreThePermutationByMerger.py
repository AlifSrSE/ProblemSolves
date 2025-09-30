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
        sequence_length = 2 * n
        v = []
        s = set()
        
        for i in range(sequence_length):
            x = int(data[pointer + i])
            if x not in s:
                v.append(x)
                s.add(x)
        
        pointer += sequence_length
        output.append(" ".join(map(str, v)))
    sys.stdout.write('\n'.join(output) + '\n')

alif()