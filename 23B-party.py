# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/23/B

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(n - 2 if n > 2 else 0)

solve()