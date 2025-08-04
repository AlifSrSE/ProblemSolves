# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1269/A

import sys

def alif():
    n = int(sys.stdin.readline())
    
    if n % 2 != 0:
        b = 9
    else:
        b = 4
    
    sys.stdout.write(f"{n + b} {b}\n")

if __name__ == "__main__":
    alif()