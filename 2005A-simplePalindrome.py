# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
VOWELS = "aeiou"

def solve(n):
    return ''.join(VOWELS[i] * (n // len(VOWELS) + (1 if i < n % len(VOWELS) else 0))
                  for i in range(len(VOWELS)))

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        results.append(solve(n))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()