# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/276/D

def solve():
    a, b = map(int, input().split())
    s = a ^ b
    d = 1
    while d <= s:
        d *= 2
    print(d - 1)

if __name__ == "__main__":
    solve()