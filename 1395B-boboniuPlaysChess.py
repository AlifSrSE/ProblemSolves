# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    x = int(data[2])
    y = int(data[3])
    output = []

    for row in range(1, n + 1):
        r_prime = 1 + (row + x - 2) % n
        
        if row % 2 == 1:
            for col in range(1, m + 1):
                c_prime = 1 + (col + y - 2) % m
                output.append(f"{r_prime} {c_prime}")
        else:
            for col in range(m, 0, -1):
                c_prime = 1 + (col + y - 2) % m
                output.append(f"{r_prime} {c_prime}")

    sys.stdout.write('\n'.join(output) + '\n')

alif()
