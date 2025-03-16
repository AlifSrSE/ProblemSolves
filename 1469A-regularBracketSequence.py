# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1469/problem/A

def solve():
  s = input()
  if len(s) % 2 != 0 or s[0] == ')' or s[-1] == '(':
    print("NO")
  else:
    print("YES")

t = int(input())
for _ in range(t):
  solve()