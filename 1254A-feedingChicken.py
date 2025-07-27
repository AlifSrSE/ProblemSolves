# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1254/problem/A

import sys

def get_char(x):
    if x < 10:
        return chr(ord('0') + x)
    elif x < 36:
        return chr(ord('a') + x - 10)
    elif x < 62:
        return chr(ord('A') + x - 36)
    else:
        return '#'

def alif():
    t = int(sys.stdin.readline())

    while t > 0:
        r, c, k = map(int, sys.stdin.readline().split())
        grid_data = []
        for row_idx in range(r):
            grid_data.append(list(sys.stdin.readline().strip()))
        
        total_rice = 0
        for row_idx in range(r):
            for col_idx in range(c):
                if grid_data[row_idx][col_idx] == 'R':
                    total_rice += 1
        
        base_rice_per_person = total_rice // k
        extra_rice_people_count = total_rice % k
        current_person_id = 0
        target_rice_for_current_person = base_rice_per_person + (1 if current_person_id < extra_rice_people_count else 0)
        
        for row_idx in range(r):
            if row_idx % 2 == 0:
                col_start, col_stop, col_step = 0, c, 1
            else:
                col_start, col_stop, col_step = c - 1, -1, -1
            
            for col_idx in range(col_start, col_stop, col_step):
                has_rice = (grid_data[row_idx][col_idx] == 'R')
                grid_data[row_idx][col_idx] = get_char(current_person_id)
                
                if has_rice:
                    target_rice_for_current_person -= 1
                    
                    if target_rice_for_current_person <= 0:
                        current_person_id += 1 

                        if current_person_id >= k:
                            current_person_id = k - 1
                        
                        target_rice_for_current_person = base_rice_per_person + (1 if current_person_id < extra_rice_people_count else 0)
            
        for row_idx in range(r):
            sys.stdout.write("".join(grid_data[row_idx]) + "\n")
        
        t -= 1

if __name__ == "__main__":
    alif()