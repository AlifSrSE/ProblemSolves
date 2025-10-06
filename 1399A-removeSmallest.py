# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = sys.stdin.read().split()
    if not data:
        return

    t = int(data[0])
    data_idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        a = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        a.sort()
        res = True
        
        for p in range(1, n):
            if a[p] - a[p-1] > 1:
                res = False
                break
                
        if res:
            results.append("YES")
        else:
            results.append("NO")
            
    sys.stdout.write('\n'.join(results) + '\n')

alif()
