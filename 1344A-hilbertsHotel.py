# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str: return
    t = int(t_str)
    for _ in range(t):
        n_str = sys.stdin.readline()
        if not n_str: continue
        n = int(n_str)
        a_str = sys.stdin.readline()
        if not a_str: continue
        a = list(map(int, a_str.split()))
        
        visited = [False] * n
        is_permutation = True
        
        for p in range(n):
            target_index = (p + (a[p] % n) + n) % n
            
            if visited[target_index]:
                is_permutation = False
                
            visited[target_index] = True
            
        if is_permutation:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()