# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a, b):
    return "Bob" if a == b or a == b[::-1] else "Alice"

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        b = list(map(int, input[ptr:ptr+n]))
        ptr += n
        print(solve(a, b))

if __name__ == "__main__":
    main()