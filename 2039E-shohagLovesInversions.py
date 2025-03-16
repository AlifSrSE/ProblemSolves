import sys

N = 1000009
mod = 998244353
dp = [0] * N

def solve():
  n = int(sys.stdin.readline().strip())
  sum_val = 0
  for i in range(n, 0, -1):
    dp[i] = (i * sum_val + 1) % mod
    sum_val = (sum_val + dp[i]) % mod

  ans = n - 1
  for k in range(3, n + 1):
    ways = ((k - 1) * (k - 2) // 2 - 1 + mod) % mod
    ans = (ans + ways * dp[k]) % mod

  print(ans)

def main():
  t = int(sys.stdin.readline().strip())
  for _ in range(t):
    solve()

if __name__ == "__main__":
  main()