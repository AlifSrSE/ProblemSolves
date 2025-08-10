# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1294/problem/B

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n_str = sys.stdin.readline()
            if not n_str: break
            n = int(n_str)
            points = []

            for _ in range(n):
                x, y = map(int, sys.stdin.readline().split())
                points.append((x, y))
        except (IOError, ValueError):
            continue

        points.sort()
        possible = True
        path = []
        current_x, current_y = 0, 0

        for target_x, target_y in points:
            if target_y < current_y:
                possible = False
                break
            
            right_moves = target_x - current_x
            path.extend(['R'] * right_moves)
            current_x = target_x
            up_moves = target_y - current_y
            path.extend(['U'] * up_moves)
            current_y = target_y
        
        if possible:
            print("YES")
            print("".join(path))
        else:
            print("NO")

if __name__ == "__main__":
    alif()