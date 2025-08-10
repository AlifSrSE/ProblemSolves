# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1283/problem/C

import sys

def alif():
    try:
        n = int(sys.stdin.readline())
        f = [0] + list(map(int, sys.stdin.readline().split()))
        
    except (IOError, ValueError):
        return

    g = [0] * (n + 1)
    for p in range(1, n + 1):
        if f[p] != 0:
            g[f[p]] = p

    singles = []
    h = [False] * (n + 1)
    
    for p in range(1, n + 1):
        if f[p] == 0 and g[p] == 0:
            singles.append(p)
            h[p] = True

    for p in range(1, n + 1):
        if h[p]:
            continue

        left = p
        right = p
        h[p] = True

        while f[right] != 0 and not h[f[right]]:
            right = f[right]
            h[right] = True

        while g[left] != 0 and not h[g[left]]:
            left = g[left]
            h[left] = True
        
        if f[right] != 0:
            continue

        if singles:
            f[right] = singles.pop()
            f_right = f[right]
            while singles:
                f[f_right] = singles.pop()
                f_right = f[f_right]
            f[f_right] = left
        else:
            f[right] = left

    ss = len(singles)
    if ss > 0:
        for p in range(ss):
            f[singles[p]] = singles[(p + 1) % ss]

    sys.stdout.write(" ".join(map(str, f[1:])) + "\n")

if __name__ == "__main__":
    alif()