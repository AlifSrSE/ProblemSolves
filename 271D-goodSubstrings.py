# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/271/D

def solve():
    n_val = 26
    b_val = 256
    s = input()
    t = input()
    k = int(input())
    n = len(s)
    bad = [False] * b_val
    for p in range(n_val):
        bad[ord('a') + p] = (t[p] == '0')

    cb = [0] * n
    for p in range(n):
        cb[p] = (cb[p - 1] if p > 0 else 0) + bad[ord(s[p])]

    f = set()
    for p in range(n):
        for q in range(p, n):
            length = q - p + 1
            bad_count = cb[q] - (cb[p - 1] if p > 0 else 0)
            if bad_count <= k:
                f.add(s[p : q + 1])

    print(len(f))

if __name__ == "__main__":
    solve()