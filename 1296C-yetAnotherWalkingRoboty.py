# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1296/problem/C

import sys

def alif():
    try:
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
    except (IOError, ValueError):
        return

    positions = {(0, 0): 0}
    x, y = 0, 0
    min_len = float('inf')
    best_start, best_stop = -1, -1

    for i, move in enumerate(s):
        if move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        
        current_pos = (x, y)
        
        if current_pos in positions:
            prev_index = positions[current_pos]
            current_len = (i + 1) - prev_index

            if current_len < min_len:
                min_len = current_len
                best_start = prev_index + 1
                best_stop = i + 1
        positions[current_pos] = i + 1
    if best_start != -1:
        print(best_start, best_stop)
    else:
        print(-1)

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()