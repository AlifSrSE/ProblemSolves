# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/2034/B

def solve(s, m, k):
    result = 0
    index = 0
    zero_count = 0
    while index < len(s):
        if s[index] == '0':
            zero_count += 1
            if zero_count == m:
                result += 1
                zero_count = 0
                index += k
            else:
                index += 1
        else:
            zero_count = 0
            index += 1
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        _, m, k = map(int, input().split())
        s = input()
        print(solve(s, m, k))