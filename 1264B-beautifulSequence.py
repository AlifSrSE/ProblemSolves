# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1264/B

import sys

def alif(start_val, a_init, b_init, c_init, d_init):
    counts = [a_init, b_init, c_init, d_init]
    
    if counts[start_val] == 0:
        return None

    sequence = [start_val]
    counts[start_val] -= 1
    current_val = start_val

    while sum(counts) > 0:
        next_val = -1
        if current_val == 0:
            if counts[1] > 0:
                next_val = 1
        elif current_val == 3:
            if counts[2] > 0:
                next_val = 2
        elif current_val == 1:
            can_go_0 = (counts[0] > 0)
            can_go_2 = (counts[2] > 0)
            
            if can_go_0 and can_go_2:
                if counts[0] == 1 and counts[2] == 1 and counts[3] == 0:
                    next_val = 0
                elif counts[0] > counts[2]:
                    next_val = 0
                else:
                    next_val = 2
            elif can_go_0:
                next_val = 0
            elif can_go_2:
                next_val = 2
        elif current_val == 2:
            can_go_1 = (counts[1] > 0)
            can_go_3 = (counts[3] > 0)
            
            if can_go_1 and can_go_3:
                if counts[1] == 1 and counts[3] == 1 and counts[0] == 0:
                    next_val = 3
                elif counts[1] > counts[3]:
                    next_val = 1
                else:
                    next_val = 3
            elif can_go_1:
                next_val = 1
            elif can_go_3:
                next_val = 3
        
        if next_val != -1 and counts[next_val] > 0:
            sequence.append(next_val)
            counts[next_val] -= 1
            current_val = next_val
        else:
            return None
            
    return sequence

def alif():
    a, b, c, d = map(int, sys.stdin.readline().split())
    initial_counts = [a, b, c, d]
    res = alif(0, *initial_counts)

    if res:
        print("YES")
        print(*res)
        return
    
    res = alif(1, *initial_counts)
    if res:
        print("YES")
        print(*res)
        return
    
    res = alif(2, *initial_counts)
    if res:
        print("YES")
        print(*res)
        return
    
    res = alif(3, *initial_counts)
    if res:
        print("YES")
        print(*res)
        return
    print("NO")

if __name__ == "__main__":
    alif()