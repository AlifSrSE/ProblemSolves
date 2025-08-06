# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1279/C

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        s = {}

        for p in range(m):
            s[b[p]] = p
        d = [0] * m 

        for p in range(n):
            if a[p] in s:
                d[s[a[p]]] = p

        mx = 0
        prev = 0
        cnt = 0

        for p in range(m):
            if d[p] >= mx:
                mx = d[p]
                cnt += 2 * (d[p] - prev) + 1
                prev += 1
            else:
                cnt += 1
        
        sys.stdout.write(f"{cnt}\n")

if __name__ == "__main__":
    alif()