# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
import collections

sys.setrecursionlimit(200000)

def alif():
    t = int(sys.stdin.readline())
    results = []
    for _ in range(t):
        n_line = sys.stdin.readline()
        if not n_line:
            break
        n = int(n_line)
        a = list(map(int, sys.stdin.readline().split()))

        zero_indices = [i for i, x in enumerate(a) if x == 0]
        Z = len(zero_indices)

        if Z < 2:
            results.append(0)
            continue
            
        H = Z // 2
        L_indices = zero_indices[:H]
        R_indices = zero_indices[Z - H:]
        unique_non_zero_values = {}
        for x in a:
            if x != 0:
                unique_non_zero_values[x] = 1
        
        non_zero_counts = collections.defaultdict(int)
        for x in a:
            if x != 0:
                non_zero_counts[x] += 1
        
        non_zeros = []
        for i, x in enumerate(a):
            if x != 0:
                non_zeros.append((i, x))
                
        value_to_indices = collections.defaultdict(list)
        for i, x in enumerate(a):
            if x != 0:
                value_to_indices[x].append(i)

        m = H
        non_zeros_info = []
        for i, x in enumerate(a):
            if x != 0:
                non_zeros_info.append((i, x))
                
        unique_non_zero_count = len(unique_non_zero_values)
        m = H
        unique_values = sorted(list(unique_non_zero_values.keys()))
        m_ans = min(H, unique_non_zero_count)
        ans = min(H, len(unique_non_zero_values))
        results.append(ans)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
alif()