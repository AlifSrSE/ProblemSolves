# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve(a, b):
    return 6 - a - b

def main():
    input = sys.stdin.read().split()
    a = int(input[0])
    b = int(input[1])
    print(solve(a, b))

if __name__ == "__main__":
    main()