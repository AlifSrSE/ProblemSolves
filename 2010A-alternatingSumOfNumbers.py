# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a):
    return sum(a[i] if i % 2 == 0 else -a[i] for i in range(len(a)))

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        results.append(str(solve(a)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()