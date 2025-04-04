# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from collections import Counter

def solve(a):
    value_to_count = Counter(a)
    return max(value_to_count.values())

def main():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(a))

if __name__ == "__main__":
    main()