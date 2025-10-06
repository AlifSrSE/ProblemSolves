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
    results = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        a = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        b = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        mina = min(a)
        minb = min(b)
        cnt = 0
        
        for p in range(n):
            x = a[p] - mina
            y = b[p] - minb
            cnt += max(x, y)

        results.append(str(cnt))

    sys.stdout.write('\n'.join(results) + '\n')

alif()
