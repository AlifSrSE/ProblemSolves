# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1250/problem/L

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().split())
        m = (a + b + c + 2) // 3
        ans = m 

        if a >= b or c >= b:
            if a < c:
                a, c = c, a

            if c < m:
                b -= (m - c)
                b = max(0, b)
                
            m = max(m, c)
            x = (a + b + 1) // 2
            ans = max(m, x)

        sys.stdout.write(f"{ans}\n")

if __name__ == "__main__":
    alif()