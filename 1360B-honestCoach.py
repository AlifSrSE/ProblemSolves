# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        s = list(map(int, sys.stdin.readline().split()))
        s.sort()
        min_diff = float('inf')
        for i in range(1, n):
            diff = s[i] - s[i-1]
            min_diff = min(min_diff, diff)
        print(min_diff)

if __name__ == "__main__":
    alif()