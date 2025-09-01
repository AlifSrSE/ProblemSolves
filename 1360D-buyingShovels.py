# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
import math

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        max_valid_divisor = 1

        for p in range(1, int(math.sqrt(n)) + 1):
            if n % p == 0:
                if p <= k:
                    max_valid_divisor = max(max_valid_divisor, p)

                other_divisor = n // p
                if other_divisor <= k:
                    max_valid_divisor = max(max_valid_divisor, other_divisor)

        result = n // max_valid_divisor
        print(result)

if __name__ == "__main__":
    alif()