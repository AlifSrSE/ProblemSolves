# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
import math

def solve(n, x, y):
    return max(math.ceil(n / x), math.ceil(n / y))

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        x = int(input[ptr])
        ptr += 1
        y = int(input[ptr])
        ptr += 1
        results.append(str(solve(n, x, y)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()