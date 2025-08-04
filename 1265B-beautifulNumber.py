# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1265/B

import sys

def alif():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        pos_of_val = [0] * (n + 2)
        input_permutation = list(map(int, sys.stdin.readline().split()))

        for p in range(n):
            pos_of_val[input_permutation[p]] = p + 1
            
        is_active_pos = [False] * (n + 2)
        num_segments = 0
        results = []
        
        for p_val in range(1, n + 1):
            current_val_pos = pos_of_val[p_val]
            is_active_pos[current_val_pos] = True
            left_neighbor_active = is_active_pos[current_val_pos - 1]
            right_neighbor_active = is_active_pos[current_val_pos + 1]
            
            if not left_neighbor_active and not right_neighbor_active:
                num_segments += 1

            elif left_neighbor_active and right_neighbor_active:
                num_segments -= 1
            results.append('1' if num_segments <= 1 else '0')
        sys.stdout.write("".join(results) + "\n")

if __name__ == "__main__":
    alif()