# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
import math

def solve(c, a, b):
    g = math.gcd(a, b)
    remainders = [ci % g for ci in c]
    remainders.sort()
    max_diff = 0
    for i in range(len(remainders)):
        diff = (remainders[(i + 1) % len(remainders)] - remainders[i]) % g
        if diff > max_diff:
            max_diff = diff
    return 0 if max_diff == 0 else (g - max_diff)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = int(input[ptr])
        ptr += 1
        b = int(input[ptr])
        ptr += 1
        c = list(map(int, input[ptr:ptr + n]))
        ptr += n
        results.append(str(solve(c, a, b)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()