# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    sys.stdin.readline()
    t_cases = int(sys.stdin.readline())
    for _ in range(t_cases):
        h, c, t = map(int, sys.stdin.readline().split())

        if t >= h:
            print(1)
            continue
        
        if 2 * t <= h + c:
            print(2)
            continue
        
        n = (h - t) // (2 * t - c - h)
        diff1 = abs(((n + 1) * h + n * c) / (2 * n + 1) - t)
        diff2 = abs(((n + 2) * h + (n + 1) * c) / (2 * n + 3) - t)

        if diff2 < diff1:
            print(2 * (n + 1) + 1)
        else:
            print(2 * n + 1)

if __name__ == "__main__":
    alif()