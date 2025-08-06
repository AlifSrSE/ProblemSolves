# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1272/B

import sys

def alif():
    q = int(sys.stdin.readline())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        u_count = 0
        d_count = 0
        l_count = 0
        r_count = 0

        for char in s:
            if char == 'U':
                u_count += 1
            elif char == 'D':
                d_count += 1
            elif char == 'L':
                l_count += 1
            elif char == 'R':
                r_count += 1
        
        min_ud = min(u_count, d_count)
        u_count = min_ud
        d_count = min_ud
        min_lr = min(l_count, r_count)
        l_count = min_lr
        r_count = min_lr

        if u_count == 0 and l_count > 0:
            l_count = 1
            r_count = 1
        
        if r_count == 0 and u_count > 0:
            u_count = 1
            d_count = 1
        
        sys.stdout.write(f"{u_count + d_count + l_count + r_count}\n")
        sys.stdout.write("U" * u_count)
        sys.stdout.write("L" * l_count)
        sys.stdout.write("D" * d_count)
        sys.stdout.write("R" * r_count)
        sys.stdout.write("\n")

if __name__ == "__main__":
    alif()