# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a, c, l, r):
    max_val = max(a)
    result = []
    for i in range(len(c)):
        if l[i] <= max_val <= r[i]:
            if c[i] == '+':
                max_val += 1
            else:
                max_val -= 1
        result.append(str(max_val))
    return ' '.join(result)

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
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        c = []
        l = []
        r = []
        for _ in range(m):
            c.append(input[ptr])
            ptr += 1
            l.append(int(input[ptr]))
            ptr += 1
            r.append(int(input[ptr]))
            ptr += 1
        results.append(solve(a, c, l, r))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()