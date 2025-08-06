# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1270/C

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        a_values = list(map(int, sys.stdin.readline().split()))
        s = 0
        x = 0
        
        for val in a_values:
            s += val
            x ^= val
        
        sys.stdout.write("2\n")
        sys.stdout.write(f"{s + x} {x}\n")

if __name__ == "__main__":
    alif()