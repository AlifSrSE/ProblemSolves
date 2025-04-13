# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(x):
    return len(x) == 2 and x[1] - x[0] >= 2

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        x = list(map(int, input[ptr:ptr+n]))
        ptr += n
        results.append("YES" if solve(x) else "NO")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()