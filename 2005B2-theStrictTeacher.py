# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
import bisect

def solve(n, b, a):
    b_sorted = sorted(b)
    results = []
    for ai in a:
        if ai < b_sorted[0]:
            results.append(str(b_sorted[0] - 1))
        elif ai > b_sorted[-1]:
            results.append(str(n - b_sorted[-1]))
        else:
            index = bisect.bisect_left(b_sorted, ai)
            results.append(str((b_sorted[index] - b_sorted[index - 1]) // 2))
    return '\n'.join(results)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    output = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        m = int(input[ptr])
        ptr += 1
        q = int(input[ptr])
        ptr += 1
        b = list(map(int, input[ptr:ptr+m]))
        ptr += m
        a = list(map(int, input[ptr:ptr+q]))
        ptr += q
        output.append(solve(n, b, a))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()