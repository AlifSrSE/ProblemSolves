# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1294/problem/C

import sys
import math

def alif():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n_orig = int(sys.stdin.readline())
        except (IOError, ValueError):
            continue
        n = n_orig
        a, b, c = 1, 1, 1

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                a = i
                n //= a
                break

        if a == 1:
            print("NO")
            continue

        for i in range(a + 1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                b = i
                n //= b
                break
        c = n

        if b > 1 and c > 1 and a != b and a != c and b != c:
            print("YES")
            print(f"{a} {b} {c}")
        else:
            print("NO")

if __name__ == "__main__":
    alif()