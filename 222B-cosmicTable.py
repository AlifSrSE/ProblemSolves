# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr + 1])
    k = int(input[ptr + 2])
    ptr += 3

    table = []
    for _ in range(n):
        row = list(map(int, input[ptr:ptr + m]))
        ptr += m
        table.append(row)

    row_map = [i for i in range(n + 1)]  
    col_map = [i for i in range(m + 1)] 

    output = []
    for _ in range(k):
        query = input[ptr]
        x = int(input[ptr + 1])
        y = int(input[ptr + 2])
        ptr += 3
        if query == 'c':
            col_map[x], col_map[y] = col_map[y], col_map[x]
        elif query == 'r':
            row_map[x], row_map[y] = row_map[y], row_map[x]
        elif query == 'g':
            original_row = row_map[x]
            original_col = col_map[y]
            output.append(str(table[original_row - 1][original_col - 1]))
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()