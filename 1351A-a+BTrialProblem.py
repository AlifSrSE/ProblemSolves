# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)

if __name__ == "__main__":
    alif()