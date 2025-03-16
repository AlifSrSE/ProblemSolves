# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1896/problem/A

def solve():
  n = int(input())
  a = list(map(int, input().split()))
  msg = "YES"
  while True:
    f = 0
    for i in range(1, n - 1):
      if a[i] > a[i - 1] and a[i] > a[i + 1]:
        a[i], a[i + 1] = a[i + 1], a[i]
        f = 1
    if all(a[i] <= a[i+1] for i in range(n-1)):
      break
    if f == 0 and not all(a[i] <= a[i+1] for i in range(n-1)):
      msg = "NO"
      break
  print(msg)

t = int(input())
for _ in range(t):
  solve()