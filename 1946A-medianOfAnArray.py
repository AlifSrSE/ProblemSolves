# Author: AlifSrSe
# date: 2025-03-21
# https://codeforces.com/problemset/problem/1946/A
 
def solve(a):
    a.sort()
    median = a[(len(a) - 1) // 2]
    return sum(1 for x in a[(len(a) - 1) // 2:] if x == median)
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))