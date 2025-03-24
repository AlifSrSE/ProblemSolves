# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/2034/A

def solve(a, b):
    i = min(a, b)
    while True:
        if i % a == i % b:
            return i
        i += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(solve(a, b))