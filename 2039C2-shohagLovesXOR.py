import sys

def solve():
  x, m = map(int, sys.stdin.readline().split())

  # divisible by x
  p = m - m % x
  ans = p // x - (x < p)
  if 1 <= (x ^ p) <= m:
    ans += 1
  p += x
  if 1 <= (x ^ p) <= m:
    ans += 1

  # divisibly by y
  for y in range(1, min(x, m) + 1):
    cur = x ^ y
    if cur % y == 0:
      ans += 1

  # divisible by both
  if x <= m:
    ans -= 1

  print(ans)

def main():
  t = int(sys.stdin.readline().strip())
  for _ in range(t):
    solve()

if __name__ == "__main__":
  main()