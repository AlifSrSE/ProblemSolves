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
        A = int(data[data_idx])
        data_idx += 1
        B = int(data[data_idx])
        data_idx += 1
        X = int(data[data_idx])
        data_idx += 1
        Y = int(data[data_idx])
        data_idx += 1
        N = int(data[data_idx])
        data_idx += 1

        n_a = N
        a_a = A
        b_a = B
        
        u_a1 = min(a_a - X, n_a)
        a_a -= u_a1
        n_a -= u_a1
        
        u_a2 = min(b_a - Y, n_a)
        b_a -= u_a2        
        resA = a_a * b_a

        n_b = N
        a_b = A
        b_b = B
        
        u_b1 = min(b_b - Y, n_b)
        b_b -= u_b1
        n_b -= u_b1

        u_b2 = min(a_b - X, n_b)
        a_b -= u_b2
        resB = a_b * b_b
        res = min(resA, resB)
        output_lines.append(str(res))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
