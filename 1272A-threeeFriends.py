# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1272/A

import sys

def alif():
    q = int(sys.stdin.readline())
    
    for _ in range(q):
        x = list(map(int, sys.stdin.readline().split()))
        x.sort()
        
        if x[0] < x[2]:
            x[0] += 1
        
        if x[1] < x[2]:
            x[1] += 1
        
        if x[2] > x[0]:
            x[2] -= 1
        
        ans = 2 * (x[2] - x[0])
        sys.stdout.write(f"{ans}\n")

if __name__ == "__main__":
    alif()