# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        cnt = 1
        for p in range(n - 1, -1, -1):
            if a[p] <= p + 1:
                cnt = p + 2
                break
        print(cnt)

if __name__ == "__main__":
    alif()