# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    n = int(input())
    p = [0] * (n + 1)
    used = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if used[i]:
            continue
        cycle = [i]
        used[i] = True
        curr = i
        
        while True:
            min_mod = n + 1
            next_idx = -1
            for j in range(1, n + 1):
                if not used[j]:
                    print(f"? {curr} {j}", flush=True)
                    mod = int(input())
                    if mod < min_mod:
                        min_mod = mod
                        next_idx = j
            if next_idx == -1:
                break
            cycle.append(next_idx)
            used[next_idx] = True
            curr = next_idx
        
        if len(cycle) == 1:
            p[cycle[0]] = cycle[0]
        else:
            for j in range(len(cycle)):
                p[cycle[j]] = cycle[(j + 1) % len(cycle)]
    
    print("!", *p[1:], flush=True)

alif()