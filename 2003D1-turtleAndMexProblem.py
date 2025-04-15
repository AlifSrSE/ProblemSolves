# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a, m):
    def calculate_mex(arr):
        seen = set(arr)
        mex = 0
        missing_seen = False
        while True:
            if mex not in seen:
                if missing_seen:
                    return mex
                missing_seen = True
            mex += 1

    base_value = max(calculate_mex(ai) for ai in a)
    base_length = min(m + 1, base_value + 1)

    if base_value <= m:
        sum_part = (base_value + 1 + m) * (m - base_value) // 2
    else:
        sum_part = 0

    return base_value * base_length + sum_part

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        m = int(input[ptr])
        ptr += 1
        a = []
        for _ in range(n):
            l = int(input[ptr])
            ptr += 1
            row = list(map(int, input[ptr:ptr+l]))
            ptr += l
            a.append(row)
        
        results.append(str(solve(a, m)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()