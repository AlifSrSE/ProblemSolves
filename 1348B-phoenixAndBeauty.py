# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        nk_str = sys.stdin.readline()
        if not nk_str:
            continue
        n, k = map(int, nk_str.split())

        a_str = sys.stdin.readline()
        if not a_str:
            continue
        a = list(map(int, a_str.split()))
        
        unique_elements = sorted(list(set(a)))
        
        if len(unique_elements) > k:
            print("-1")
            continue
            
        result_array = []
        for p in range(n):
            current_elements = unique_elements[:]
            while len(current_elements) < k:
                current_elements.append(1)
            result_array.extend(current_elements)
            
        print(len(result_array))
        print(*result_array)

if __name__ == "__main__":
    alif()