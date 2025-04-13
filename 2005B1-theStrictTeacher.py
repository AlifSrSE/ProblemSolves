# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(n, b, a):
    min_b = min(b[0], b[1])
    max_b = max(b[0], b[1])
    
    if a[0] < min_b:
        return min_b - 1
    if a[0] > max_b:
        return n - max_b
    
    return (max_b - min_b) // 2

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
        q = int(input[ptr])
        ptr += 1
        b = list(map(int, input[ptr:ptr+m]))
        ptr += m
        a = list(map(int, input[ptr:ptr+q]))
        ptr += q
        results.append(str(solve(n, b, a)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()