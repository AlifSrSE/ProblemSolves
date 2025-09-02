# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
import math

def alif():
    n, m, a, b = map(int, sys.stdin.readline().split())

    if n * a != m * b:
        print("NO")
        return

    print("YES")
    shift = m // math.gcd(n, m)
    s = '1' * a + '0' * (m - a)
    
    for _ in range(n):
        print(s)
        s = s[shift:] + s[:shift]

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()