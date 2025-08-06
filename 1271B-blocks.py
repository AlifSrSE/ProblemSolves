# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1271/B

import sys

def alif():
    n = int(sys.stdin.readline())
    s_list = list(sys.stdin.readline().strip())

    w_count = s_list.count('W')
    b_count = s_list.count('B')

    target_char = None
    if w_count % 2 == n % 2:
        target_char = 'W'
    elif b_count % 2 == n % 2:
        target_char = 'B'

    v = []
    if target_char:
        for p in range(n - 1):
            if s_list[p] == target_char:
                continue
            s_list[p] = target_char
            v.append(p + 1)
            if s_list[p + 1] == 'W':
                s_list[p + 1] = 'B'
            elif s_list[p + 1] == 'B':
                s_list[p + 1] = 'W'

    if target_char:
        sys.stdout.write(f"{len(v)}\n")
        sys.stdout.write(" ".join(map(str, v)) + "\n")
    else:
        sys.stdout.write("-1\n")

if __name__ == "__main__":
    alif()