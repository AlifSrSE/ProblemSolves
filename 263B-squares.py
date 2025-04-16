# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/263/B

def solve():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort()
    if k > n or (k < n - 1 and s[n - k] == s[n - k - 1]):
        print("-1")
    else:
        print(s[n - k], 0)

solve()