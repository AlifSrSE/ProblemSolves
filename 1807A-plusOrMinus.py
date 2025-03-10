# Author : AlifSrSE
# Date : 2025-03-10
# Problem link : https://codeforces.com/contest/1807/problem/A

import sys
input = sys.stdin.readline

def main():
    t = int(input().strip())
    for _ in range(t):
        a, b, c = map(int, input().strip().split())
        if a + b == c:
            print("+")
        else:
            print("-")

if __name__ == "__main__":
    main()