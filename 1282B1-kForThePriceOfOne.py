# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1282/B1

import sys

def solve():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n, v, k = map(int, sys.stdin.readline().split())
            a = list(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            continue

        a.sort()
        mx = 0

        for p in range(k):
            left = 0
            if p > 0:
                left = sum(a[:p])

            if v < left:
                break

            tst = left
            idx = p
            
            while (idx + k <= n) and (tst + a[idx + k - 1] <= v):
                tst += a[idx + k - 1]
                idx += k
            
            mx = max(mx, idx)
        print(mx)

if __name__ == "__main__":
    solve()