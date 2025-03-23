# Author: AlifSrSe
# date: 2025-03-19
# https://codeforces.com/problemset/problem/1971/A

def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        print(min(x, y), max(x, y))

if __name__ == "__main__":
    main()