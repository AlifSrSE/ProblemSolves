import sys

N = 1000009
mod = 998244353

def add(x, y):
    res = x + y
    if res >= mod:
        res -= mod
    return res

spf = [0] * N

def sieve():
    p = []
    for i in range(2, N):
        if spf[i] == 0:
            spf[i] = i
            p.append(i)
        for j in range(len(p)):
            if i * p[j] >= N or p[j] > spf[i]:
                break
            spf[i * p[j]] = p[j]

mob = [0] * N

def mobius():
    mob[1] = 1
    for i in range(2, N):
        mob[i] -= 1
        for j in range(i + i, N, i):
            mob[j] -= mob[i]
    for i in range(1, N):
        mob[i] = (mob[i] % mod + mod) % mod

c = [0] * N
divs = [[] for _ in range(N)]

def gen_divs(n):
    id_val = 1
    x = n
    divs[n][0] = 1
    while n > 1:
        k = spf[n]
        cur = 1
        sz = id_val
        while n % k == 0:
            cur *= k
            n //= k
            for i in range(sz):
                divs[x][id_val] = divs[x][i] * cur
                id_val += 1

def prec():
    sieve()
    for i in range(1, N):
        for j in range(i, N, i):
            c[j] += 1
        divs[i] = [0] * c[i]
        gen_divs(i)
    mobius()

dp = [0] * N
f = [0] * N
tmp = [0] * N
ans = [0] * N

def solve():
    for i in range(1, N):
        for d in divs[i]:
            tmp[d] = (mod - f[d]) % mod
            for c_val in divs[d]:
                tmp[d] = add(tmp[d], dp[c_val])
            tmp[d] = (2 * tmp[d] + 1) % mod

        for d in divs[i]:
            for c_val in divs[d]:
                dp[d] = add(dp[d], (mob[c_val] * tmp[d // c_val]) % mod)
            f[d] = add(f[d], tmp[d])

        ans[i] = ans[i - 1]
        ans[i] = add(ans[i], f[i])

def main():
    prec()
    solve()
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        m = int(sys.stdin.readline().strip())
        print(ans[m])

if __name__ == "__main__":
    main()