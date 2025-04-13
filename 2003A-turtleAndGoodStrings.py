# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(s):
    return s[0] != s[-1]

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
        results.append("YES" if solve(s) else "NO")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()