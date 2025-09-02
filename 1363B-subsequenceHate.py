# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    s = sys.stdin.readline().strip()
    n = len(s)
    
    ones_prefix = [0] * (n + 1)
    zeros_prefix = [0] * (n + 1)
    
    for i in range(n):
        if s[i] == '1':
            ones_prefix[i+1] = ones_prefix[i] + 1
            zeros_prefix[i+1] = zeros_prefix[i]
        else:
            zeros_prefix[i+1] = zeros_prefix[i] + 1
            ones_prefix[i+1] = ones_prefix[i]

    total_ones = ones_prefix[n]
    total_zeros = zeros_prefix[n]
    
    result = min(total_ones, total_zeros)
    
    for i in range(n + 1):
        cost1 = ones_prefix[i] + (total_zeros - zeros_prefix[i])
        cost2 = zeros_prefix[i] + (total_ones - ones_prefix[i]) 
        result = min(result, cost1, cost2)
    print(result)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
