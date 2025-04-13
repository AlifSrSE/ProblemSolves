# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a, k):
    sorted_a = sorted(a, reverse=True)
    alt_sum = sum(sorted_a[i] if i % 2 == 0 else -sorted_a[i] for i in range(len(sorted_a)))
    pair_diff_sum = sum(sorted_a[i*2] - sorted_a[i*2+1] for i in range(len(sorted_a)//2))
    
    return alt_sum - min(k, pair_diff_sum)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        k = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        results.append(str(solve(a, k)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()