# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1999/A

def solve(n):
    return n // 10 + n % 10

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))