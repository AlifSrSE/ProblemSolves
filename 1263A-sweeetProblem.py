# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1263/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        
        ans = 0
        if a[2] > a[0] + a[1]:
            ans = a[0] + a[1]
        else:
            ans = (a[0] + a[1] + a[2]) // 2
        
        sys.stdout.write(f"{ans}\n")

if __name__ == "__main__":
    alif()