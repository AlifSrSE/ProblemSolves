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
    
    output_lines = []
    
    for _ in range(t):
        n = int(data[data_idx])
        data_idx += 1
        x = int(data[data_idx])
        data_idx += 1
        y = int(data[data_idx])
        data_idx += 1
        
        min_max_term = float('inf')
        best_start = 0
        best_step = 0

        for s in range(1, x + 1):
            for d in range(1, y - x + 1):
                is_x_in_range = False
                if (x - s) % d == 0:
                    index_x = (x - s) // d
                    if 0 <= index_x < n:
                        is_x_in_range = True

                is_y_in_range = False
                if (y - s) % d == 0:
                    index_y = (y - s) // d
                    if 0 <= index_y < n:
                        is_y_in_range = True
                
                if not (is_x_in_range and is_y_in_range):
                    continue
                last_term = s + (n - 1) * d
                
                if last_term < min_max_term:
                    min_max_term = last_term
                    best_start = s
                    best_step = d
        
        result_ap = []
        for p in range(n):
            result_ap.append(str(best_start + p * best_step))
            
        output_lines.append(" ".join(result_ap))
        
    sys.stdout.write('\n'.join(output_lines) + '\n')

alif()
