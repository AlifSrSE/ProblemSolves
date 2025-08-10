# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1285/problem/A

import sys

def alif():
    try:
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        result = n + 1
        print(result)

    except (IOError, ValueError):
        return

if __name__ == "__main__":
    alif()
