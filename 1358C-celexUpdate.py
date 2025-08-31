# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        ans = (x2 - x1) * (y2 - y1) + 1
        print(ans)

if __name__ == "__main__":
    alif()