# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
def alif():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    data_idx = 1
    output = []
    
    for _ in range(t):
        n = int(data[data_idx])
        m = int(data[data_idx + 1])
        data_idx += 2
        
        w = []
        for _ in range(n):
            row_data = []
            for _ in range(m):
                row_data.append(int(data[data_idx]))
                data_idx += 1
            w.append(row_data)
        
        total = 0
        
        for row in range((n + 1) // 2):
            for col in range((m + 1) // 2):
                
                v = []
                v.append(w[row][col])
                
                if col != m - 1 - col:
                    v.append(w[row][m - 1 - col])
                
                if row != n - 1 - row and col != m - 1 - col:
                    v.append(w[n - 1 - row][m - 1 - col])
                
                if row != n - 1 - row:
                    v.append(w[n - 1 - row][col])
                v.sort()
                median = v[len(v) // 2]
                
                for val in v:
                    total += abs(val - median)
        
        total_abs_diff = 0
        
        for row in range(n):
            for col in range(m):
                r1, c1 = row, col
                r2, c2 = row, m - 1 - col
                r3, c3 = n - 1 - row, m - 1 - col
                r4, c4 = n - 1 - row, col
                
                if r1 <= r3 and c1 <= c2:
                    group = [w[r1][c1]]
                    
                    if (r1, c1) != (r2, c2):
                        group.append(w[r2][c2])
                    if (r1, c1) != (r3, c3) and (r2, c2) != (r3, c3):
                        group.append(w[r3][c3])
                    if (r1, c1) != (r4, c4) and (r2, c2) != (r4, c4) and (r3, c3) != (r4, c4):
                        group.append(w[r4][c4])
                        
                    group = list(set(group))
                    group.sort()
                    median = group[len(group) // 2]
                    
                    for val in group:
                        total_abs_diff += abs(val - median)

        total_abs_diff_clean = 0
        for row in range((n + 1) // 2):
            for col in range((m + 1) // 2):
                
                group = []
                
                r1, c1 = row, col
                r2, c2 = row, m - 1 - col
                r3, c3 = n - 1 - row, m - 1 - col
                r4, c4 = n - 1 - row, col

                group.append(w[r1][c1])
                
                if (r1, c1) != (r2, c2):
                    group.append(w[r2][c2])
                
                if (r1, c1) != (r3, c3) and (r2, c2) != (r3, c3):
                    group.append(w[r3][c3])
                    
                if (r1, c1) != (r4, c4) and (r2, c2) != (r4, c4) and (r3, c3) != (r4, c4):
                    group.append(w[r4][c4])

                group.sort()
                median = group[len(group) // 2]
                
                cost = sum(abs(val - median) for val in group)
                total_abs_diff_clean += cost

        output.append(str(total_abs_diff_clean))
    sys.stdout.write('\n'.join(output) + '\n')
alif()