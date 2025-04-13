# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(l, r):
    return (((r - (1 - r % 2)) - (l + (1 - l % 2))) // 2 + 1) // 2

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        l = int(input[ptr])
        ptr += 1
        r = int(input[ptr])
        ptr += 1
        results.append(str(solve(l, r)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()