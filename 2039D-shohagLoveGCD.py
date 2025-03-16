import sys
import math

N = 100009
p = [0] * N

def precompute():
  for i in range(2, N):
    if p[i] != 0:
      continue
    j = i
    while j < N:
      x = j
      while x % i == 0:
        x //= i
        p[j] += 1
      j += i

def solve():
  n, m = map(int, sys.stdin.readline().split())
  s = list(map(int, sys.stdin.readline().split()))
  s.insert(0, 0)

  if m < math.floor(math.log2(n)) + 1:
    print(-1)
    return

  result = []
  for i in range(1, n + 1):
    result.append(str(s[m - p[i]]))
  print(' '.join(result))

def main():
  precompute()
  t = int(sys.stdin.readline().strip())
  for _ in range(t):
    solve()

if __name__ == "__main__":
  main()