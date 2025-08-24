# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from bisect import bisect_right

def alif():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    
    c = [a[i] - b[i] for i in range(n)]
    c.sort()
    
    ans = 0
    for i in range(n):
        ans += len(c) - bisect_right(c, -c[i], i + 1)
    
    print(ans)

if __name__ == "__main__":
    alif()