# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1260/problem/A

import sys

def alif():
    n_queries = int(sys.stdin.readline())
    for _ in range(n_queries):
        cnt, s = map(int, sys.stdin.readline().split())
        d = s // cnt
        m = s % cnt
        ans = (cnt - m) * d * d + m * (d + 1) * (d + 1)
        sys.stdout.write(f"{ans}\n")

if __name__ == "__main__":
    alif()