# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1323/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        
        if n == 1:
            x = int(sys.stdin.readline())
            if x % 2 == 0:
                print(1)
                print(1)
            else:
                print(-1)
        else:
            a = list(map(int, sys.stdin.readline().split()))
            
            if a[0] % 2 != 0 and a[1] % 2 != 0:
                print(2)
                print("1 2")
            else:
                if a[0] % 2 == 0:
                    print(1)
                    print(1)
                else:
                    print(1)
                    print(2)

alif()