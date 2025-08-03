# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : N/A

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        d = n // 14
        m = n % 14
        ans = (d >= 1) and (1 <= m) and (m <= 6)
        sys.stdout.write("YES\n" if ans else "NO\n")

if __name__ == "__main__":
    alif()