# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1999/B

def solve(a1, a2, b1, b2):
    return (is_win(a1, b1, a2, b2) + is_win(a1, b2, a2, b1)) * 2

def is_win(first_a, first_b, second_a, second_b):
    return not (first_a == first_b and second_a == second_b) and first_a >= first_b and second_a >= second_b

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a1, a2, b1, b2 = map(int, input().split())
        print(solve(a1, a2, b1, b2))