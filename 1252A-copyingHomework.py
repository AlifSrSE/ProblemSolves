# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1252/problem/A

import sys

def alif():
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    results = []
    
    for x in numbers:
        results.append(str(n + 1 - x))
    
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    alif()