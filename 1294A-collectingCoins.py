# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1294/problem/A

import sys

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    while t > 0:
        try:
            a, b, c, n = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            t -= 1
            continue

        mx = max(a, b, c)
        diff = (mx - a) + (mx - b) + (mx - c)

        if n >= diff and (n - diff) % 3 == 0:
            print("YES")
        else:
            print("NO")
        
        t -= 1

if __name__ == "__main__":
    alif()