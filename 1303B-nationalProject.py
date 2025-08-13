# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1303/problem/B

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str:
            return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n, g, b = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue

        h = (n + 1) // 2
        r = h // g
        m = h % g
        res = r * (g + b)
        if m > 0:
            res += m
        else:
            res -= b
        
        ans = max(res, n)
        print(ans)

if __name__ == "__main__":
    alif()