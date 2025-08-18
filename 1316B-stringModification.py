# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1316/problem/B

import sys

def alif():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    best_s = s
    best_k = 1

    for k in range(1, n + 1):
        prefix = s[:k-1]
        suffix = s[k-1:]
        current_s = ""

        if (n - (k - 1)) % 2 == 1:
            current_s = suffix + prefix[::-1]
        else:
            current_s = suffix + prefix
        if current_s < best_s:
            best_s = current_s
            best_k = k
    print(best_s)
    print(best_k)


def alif():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            alif()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    alif()