# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1256/problem/A

import sys

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        a, b, n, s = map(int, sys.stdin.readline().split())
        ans = (n * a + b >= s) and (b >= s % n)
        
        sys.stdout.write("YES\n" if ans else "NO\n")

if __name__ == "__main__":
    alif()