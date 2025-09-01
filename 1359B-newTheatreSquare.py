# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, x, y = map(int, sys.stdin.readline().split())
        double_cost = min(2 * x, y)
        total_cost = 0

        for _ in range(n):
            row = sys.stdin.readline().strip()
            dot_count = 0

            for char in row:
                if char == '.':
                    dot_count += 1
                else:
                    total_cost += (dot_count // 2) * double_cost
                    total_cost += (dot_count % 2) * x
                    dot_count = 0
            
            total_cost += (dot_count // 2) * double_cost
            total_cost += (dot_count % 2) * x
        print(total_cost)

if __name__ == "__main__":
    alif()