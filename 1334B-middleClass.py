# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n, x = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        a.sort(reverse=True)
        current_sum = 0
        ans = 0
        
        for i in range(n):
            current_sum += a[i]
            if current_sum >= (i + 1) * x:
                ans = i + 1
            else:
                break
        
        sys.stdout.write(str(ans) + '\n')
        t -= 1

alif()