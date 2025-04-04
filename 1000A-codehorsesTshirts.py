# Author : AlifSrSE
# Date : 2025-04-03
# Problem link : https://codeforces.com/contest/1000/problem/A

import sys

def read_array():
    return sys.stdin.readline().strip().split()

def solve(a, b):
    a_list = list(a)
    result = 0

    for bi in b:
        if bi in a_list:
            a_list.remove(bi)
        else:
            result += 1

    return result

def main():
    n = int(sys.stdin.readline().strip())
    a = read_array()
    b = read_array()
    print(solve(a, b))

if __name__ == "__main__":
    main()