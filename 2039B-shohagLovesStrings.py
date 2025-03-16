import sys

def solve():
  s = sys.stdin.readline().strip()
  n = len(s)
  for i in range(n - 1):
    if s[i] == s[i + 1]:
      print(s[i:i + 2])
      return
  for i in range(n - 2):
    if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
      print(s[i:i + 3])
      return
  print(-1)

def main():
  t = int(sys.stdin.readline().strip())
  for _ in range(t):
    solve()

if __name__ == "__main__":
  main()