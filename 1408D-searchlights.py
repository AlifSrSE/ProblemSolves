# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    MAX_COORD = 1000000
    MAX_R = MAX_COORD + 1
    robbers = []
    current_index = 2

    for _ in range(n):
        a = int(data[current_index])
        b = int(data[current_index + 1])
        robbers.append((a, b))
        current_index += 2
    searchlights = []

    for _ in range(m):
        c = int(data[current_index])
        d = int(data[current_index + 1])
        searchlights.append((c, d))
        current_index += 2
    max_y = [0] * (MAX_R + 2)

    for a_i, b_i in robbers:
        for c_j, d_j in searchlights:
            x_ij = c_j - a_i + 1
            y_ij = d_j - b_i + 1
            R_req = max(0, x_ij)
            U_req = max(0, y_ij)
            if R_req <= MAX_R:
                max_y[R_req] = max(max_y[R_req], U_req)

    for r in range(MAX_R, -1, -1):
        max_y[r] = max(max_y[r], max_y[r+1])
    min_total_moves = float('inf')
    
    for R in range(MAX_R + 1):
        U = max_y[R + 1]
        min_total_moves = min(min_total_moves, R + U)
        
    print(min_total_moves)

alif()