# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2065/problem/B
 
import sys
 
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    s = input().strip()
    same = False
    for p in range(len(s)):
        if p > 0 and s[p - 1] == s[p]:
            same = True
            break
    print(1 if same else len(s))