# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2125/problem/B

import math
def alif():
    ai, bi, ki = map(int, input().split())
    gi = math.gcd(ai, bi)
    need = max((ai + ki - 1) // ki, (bi + ki - 1) // ki)
    if gi >= need:
        print(1)
    else:
        print(2)

def main():
    ti = int(input())
    for _ in range(ti):
        alif()

if __name__ == "__main__":
    main()
