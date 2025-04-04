# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i], b[i] = map(int, input().split())

    dp = [[-1] * 3 for _ in range(n + 1)]

    def calculate(pos, in_val):
        if pos > n:
            return 0
        if dp[pos][in_val] != -1:
            return dp[pos][in_val]

        res = float('inf')
        if a[pos - 1] + in_val != a[pos]:
            res = min(res, calculate(pos + 1, 0))
        if a[pos - 1] + in_val != a[pos] + 1:
            res = min(res, b[pos] + calculate(pos + 1, 1))
        if a[pos - 1] + in_val != a[pos] + 2:
            res = min(res, 2 * b[pos] + calculate(pos + 1, 2))

        dp[pos][in_val] = res
        return res

    ans = calculate(1, 0)
    print(ans)

t = int(input())
for _ in range(t):
    solve()