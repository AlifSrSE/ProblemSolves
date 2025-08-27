# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        
        a.sort()
        b.sort(reverse=True)

        for i in range(k):
            if b[i] > a[i]:
                a[i], b[i] = b[i], a[i]
            else:
                break
        
        print(sum(a))

if __name__ == "__main__":
    alif()