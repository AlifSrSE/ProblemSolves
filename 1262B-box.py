# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1262/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        avail = [True] * (n + 1)
        possible = True
        a_input_line = list(map(int, sys.stdin.readline().split()))

        for p in range(1, n + 1):
            a[p] = a_input_line[p - 1]
            
            if a[p] < p:
                possible = False
            
            if p == 1 or a[p] > a[p-1]:
                b[p] = a[p]
                avail[a[p]] = False
        
        if possible:
            d = []
            for p in range(1, n + 1):
                if avail[p]:
                    d.append(p)
            
            idx = 0
            
            for p in range(1, n + 1):
                if b[p] > 0:
                    continue
                b[p] = d[idx]
                idx += 1
            
            sys.stdout.write(" ".join(map(str, b[1:])) + "\n")
        else:
            sys.stdout.write("-1\n")

if __name__ == "__main__":
    alif()