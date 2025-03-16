import sys

def solve():
  n = int(sys.stdin.readline().strip())
  result = []
  for i in range(1, n + 1):
    result.append(str(2 * i - 1))
  print(' '.join(result))

def main():
  t = int(sys.stdin.readline().strip())
  for _ in range(t):
    solve()

if __name__ == "__main__":
  main()