# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1980/A
 
def solve(a, m):
    return sum(max(0, m - a.count(chr(d))) for d in range(ord('A'), ord('G') + 1))

if __name__ == "__main__":
    sc = int(input())
    for _ in range(sc):
        _, m = map(int, input().split())
        a = input()
        print(solve(a, m))