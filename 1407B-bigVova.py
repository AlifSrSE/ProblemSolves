# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def alif():
    data = sys.stdin.read().split()
    if not data:
        return

    data_idx = 0
    t = int(data[data_idx])
    data_idx += 1
    
    output_lines = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        
        a = [int(x) for x in data[data_idx:data_idx + n]]
        data_idx += n
        
        b = []
        used = [False] * n
        last_gcd = 0
        
        for _ in range(n):
            best_gcd = -1
            argbest_val = -1
            argbest_idx = -1
            
            for i in range(n):
                if not used[i]:
                    current_gcd = gcd(last_gcd, a[i])
                    
                    if current_gcd > best_gcd:
                        best_gcd = current_gcd
                        argbest_val = a[i]
                        argbest_idx = i
                    elif current_gcd == best_gcd:
                        if a[i] > argbest_val:
                            argbest_val = a[i]
                            argbest_idx = i

            b.append(argbest_val)
            used[argbest_idx] = True
            last_gcd = best_gcd
            
        output_lines.append(" ".join(map(str, b)))

    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()