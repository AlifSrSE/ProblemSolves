# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(l, r, L, R):
    min_val = max(l, L)
    max_val = min(r, R)
    if min_val > max_val:
        return 1
    
    count = max_val - min_val + 1
    
    if (l <= min_val - 1 <= r) or (L <= min_val - 1 <= R):
        count += 1
    if (l <= max_val + 1 <= r) or (L <= max_val + 1 <= R):
        count += 1
    
    return count

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
        L = int(input[ptr])
        ptr += 1
        R = int(input[ptr])
        ptr += 1
        results.append(str(solve(l, r, L, R)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()