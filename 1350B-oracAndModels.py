# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        n_str = sys.stdin.readline()
        if not n_str:
            continue
        
        n = int(n_str)
        s_str = sys.stdin.readline()
        if not s_str:
            continue

        s = [0] + list(map(int, s_str.split()))
        a = [1] * (n + 1)
        max_length = 1

        for p in range(1, n + 1):
            for q in range(2 * p, n + 1, p):
                if s[p] < s[q]:
                    a[q] = max(a[q], a[p] + 1)
                    max_length = max(max_length, a[q])

        print(max_length)

if __name__ == "__main__":
    alif()