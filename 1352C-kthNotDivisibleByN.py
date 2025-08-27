# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        n, k = map(int, sys.stdin.readline().strip().split())
        result = (k // (n - 1)) * n + (k % (n - 1))

        if k % (n - 1) == 0:
            result -= 1

        print(result)

if __name__ == "__main__":
    alif()