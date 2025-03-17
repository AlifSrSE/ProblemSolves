# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2060/problem/A
 
import sys

def solve():
    a = list(map(int, sys.stdin.readline().split()))
    mx = 0
    for i in range(-200, 201):
        reconstructed_a = [a[0], a[1], i, a[2], a[3]]
        cnt = 0
        if reconstructed_a[2] == reconstructed_a[1] + reconstructed_a[0]:
            cnt += 1
        if reconstructed_a[3] == reconstructed_a[2] + reconstructed_a[1]:
            cnt += 1
        if reconstructed_a[4] == reconstructed_a[3] + reconstructed_a[2]:
            cnt += 1
        mx = max(mx, cnt)
    print(mx)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()