# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve(a, b, c):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            cost_a = float('inf')
            cost_b = float('inf')

            if i > 0:
                cost_a = dp[i - 1][j] + (0 if a[i - 1] == c[i + j - 1] else 1)
            if j > 0:
                cost_b = dp[i][j - 1] + (0 if b[j - 1] == c[i + j - 1] else 1)

            dp[i][j] = min(cost_a, cost_b)

    return dp[n][m]

def main():
    t = int(input())
    for _ in range(t):
        a = input().strip()
        b = input().strip()
        c = input().strip()
        print(solve(a, b, c))

if __name__ == "__main__":
    main()
