# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def binpow(x, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return binpow((x * x) % mod, n // 2, mod)
    return (x * binpow((x * x) % mod, n // 2, mod)) % mod

def inv(x, mod):
    return binpow(x, mod - 2, mod)

def solve():
    n = int(input())
    s = input()
    mod = 10**9 + 7
    dp = [[0, 0] for _ in range(n)]
    last_zero = -1
    dp[0][1] = (3 * inv(2, mod)) % mod
    for i in range(1, n):
        if s[i] == '0':
            dp[i][0] = (dp[i - 1][0] + 1) % mod
            dp[i][1] = ((dp[i][0] * inv(2, mod) + inv(2, mod)) % mod + (dp[i - 1][1] * inv(2, mod) + inv(2, mod)) % mod) % mod
            last_zero = i
        else:
            if last_zero == -1:
                dp[i][0] = ((i * inv(2, mod) + inv(2, mod)) % mod + (dp[i - 1][0] * inv(2, mod) + inv(2, mod)) % mod) % mod
                dp[i][1] = (((i + 1) * inv(2, mod) + inv(2, mod)) % mod + (dp[i][0] * inv(2, mod) + inv(2, mod)) % mod) % mod
            else:
                dp[i][0] = ((dp[i - 1][0] * inv(2, mod) + inv(2, mod)) % mod + ((dp[last_zero - 1][1] + i - last_zero - 1) * inv(2, mod) + inv(2, mod)) % mod) % mod
                dp[i][1] = ((dp[i][0] * inv(2, mod) + inv(2, mod)) % mod + ((dp[last_zero - 1][1] + i - last_zero) * inv(2, mod) + inv(2, mod)) % mod) % mod
    print(dp[n - 1][0])

if __name__ == "__main__":
    _t = int(input())
    for _ in range(_t):
        solve()