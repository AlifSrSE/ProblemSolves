# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1250/problem/F

import math
import sys

def alif():
    n = int(sys.stdin.readline())
    min_perimeter = float('inf')

    for p in range(1, int(math.sqrt(n)) + 1):
        if n % p == 0:
            other_side = n // p
            current_perimeter = 2 * (p + other_side)
            min_perimeter = min(min_perimeter, current_perimeter)
    
    sys.stdout.write(f"{min_perimeter}\n")

if __name__ == "__main__":
    alif()