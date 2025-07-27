# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1255/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        a_costs = list(map(int, sys.stdin.readline().split()))
        s = sum(a_costs)

        if m < n or n <= 2:
            sys.stdout.write("-1\n")
            continue
        
        sys.stdout.write(f"{2 * s}\n")
        sys.stdout.write(f"1 {n}\n")
        
        for p in range(1, n):
            sys.stdout.write(f"{p} {p + 1}\n")

if __name__ == "__main__":
    alif()