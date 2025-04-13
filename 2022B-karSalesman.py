# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def solve(a, x):
    return max(max(a), math.ceil(sum(a) / x))

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(a, x))