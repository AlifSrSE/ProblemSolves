# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1469/problem/B

def solve():
    a_list = list(map(int, input().split()))
    s = 0
    ss = 0
    for a in a_list:
        s += a
        ss = max(ss, s)
    return ss

t = int(input())
for _ in range(t):
    input()
    result1 = solve()
    input()
    result2 = solve()
    print(result1 + result2)