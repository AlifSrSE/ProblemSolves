# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1282/A

import sys

def solve():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            a, b, c, d = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue

        if a > b:
            a, b = b, a
        
        l = c - d
        r = c + d

        intersection_start = max(a, l)
        intersection_end = min(b, r)
        available_length = max(0, intersection_end - intersection_start)
        uncovered_length = (b - a) - available_length

        sys.stdout.write(str(uncovered_length) + "\n")

if __name__ == "__main__":
    solve()