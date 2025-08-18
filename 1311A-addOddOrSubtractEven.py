# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1311/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        
        if a == b:
            print(0)
        elif a < b:
            if (b - a) % 2 == 1:
                print(1)
            else:
                print(2)
        else: # a > b
            if (a - b) % 2 == 0:
                print(1)
            else:
                print(2)

if __name__ == "__main__":
    alif()