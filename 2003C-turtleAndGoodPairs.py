# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from collections import defaultdict

def solve(s):
    counts = defaultdict(int)
    for c in s:
        counts[ord(c) - ord('a')] += 1
    
    result = []
    while len(result) != len(s):
        for i in range(26):
            if counts[i] > 0:
                result.append(chr(i + ord('a')))
                counts[i] -= 1
    
    return ''.join(result)

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        ptr += 1
        s = input[ptr]
        ptr += 1
        results.append(solve(s))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()