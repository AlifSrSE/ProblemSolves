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
        weights_input = [int(data[data_idx + i]) for i in range(n)]
        data_idx += n
        
        w = [0] * (n + 1)
        for x in weights_input:
            if x <= n:
                w[x] += 1
        mx = 0
        
        for current_sum in range(2, 2 * n + 1):
            cnt = 0
            for p in range(1, n + 1):
                partner = current_sum - p
                if p > partner:
                    continue
                if partner > n:
                    continue
                if p == partner:
                    cnt += w[p] // 2
                else:
                    if partner >= 1:
                        cnt += min(w[p], w[partner])
            if cnt > mx:
                mx = cnt
        
        results.append(str(mx))

    sys.stdout.write('\n'.join(results) + '\n')

alif()
