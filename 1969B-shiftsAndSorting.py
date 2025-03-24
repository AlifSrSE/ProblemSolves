# Author: AlifSrSe
# date: 2025-03-24
# https://codeforces.com/problemset/problem/1969/B
 
def solve():
    s = input()
    ans = 0
    one = 0
    for char in s:
        if char == '0' and one:
            ans += one + 1
        elif char == '1':
            one += 1
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()