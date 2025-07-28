# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1260/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())
        ans = ((a + b) % 3 != 0) or (a > 2 * b) or (b > 2 * a)
        
        if ans:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")

if __name__ == "__main__":
    alif()