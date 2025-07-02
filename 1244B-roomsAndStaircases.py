# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1244/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        mx = n

        for p in range(n):
            if s[p] == '0':
                continue
            if 2 * p < n:
                cur = 2 * (n - p)
            else:
                cur = 2 * (p + 1)
            mx = max(mx, cur)
        sys.stdout.write(f"{mx}\n")

if __name__ == "__main__":
    alif()