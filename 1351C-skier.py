# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        s = sys.stdin.readline().strip()
        vis = set()
        cur = (0, 0)
        cnt = 0
        
        for move in s:
            next_pos = cur
            if move == 'S':
                next_pos = (next_pos[0], next_pos[1] - 1)
            elif move == 'N':
                next_pos = (next_pos[0], next_pos[1] + 1)
            elif move == 'W':
                next_pos = (next_pos[0] - 1, next_pos[1])
            elif move == 'E':
                next_pos = (next_pos[0] + 1, next_pos[1])
            
            edge = tuple(sorted((cur, next_pos)))
            
            if edge in vis:
                cnt += 1
            else:
                cnt += 5
                vis.add(edge)
            cur = next_pos

        print(cnt)

if __name__ == "__main__":
    alif()