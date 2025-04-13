# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a):
    a.sort()
    return a[len(a) // 2]

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        results.append(str(solve(a)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()