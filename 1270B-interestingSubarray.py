# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1270/B

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        pos = 0
        prev = -1

        for p in range(n):
            x = a[p]

            if pos != 0:
                continue

            if prev != -1 and abs(x - prev) > 1:
                pos = p + 1
            
            prev = x
        sys.stdout.write("YES\n" if pos != 0 else "NO\n")
        
        if pos != 0:
            sys.stdout.write(f"{pos} {pos + 1}\n")

if __name__ == "__main__":
    alif()