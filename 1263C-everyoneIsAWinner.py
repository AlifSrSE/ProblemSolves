# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1263/problem/C

import sys
import math

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = set()
        s.add(0)
        
        for p in range(1, int(math.sqrt(n)) + 1):
            s.add(p)
            s.add(n // p)   
        result_list = sorted(list(s))
        sys.stdout.write(f"{len(result_list)}\n")
        sys.stdout.write(" ".join(map(str, result_list)) + "\n")

if __name__ == "__main__":
    alif()