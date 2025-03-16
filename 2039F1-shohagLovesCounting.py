import sys

N = 200009
mod = 998244353

def add(a, b):
    a += b
    if a > mod:
        a -= mod
    if a < 0:
        a += mod
    return a

dp = [0] * N
cur = [0] * N
uni = [0] * N
sum_arr = [0] * N
d = [[] for _ in range(N)]

def precompute():
    for i in range(1, N):
        j = i
        while j < N:
            d[j].append(i)
            j += i

def solve():
    m = int(sys.stdin.readline().strip())
    for i in range(1, m + 1):
        dp[i] = cur[i] = uni[i] = sum_arr[i] = 0

    ans = 0
    for i in range(m, 0, -1):
        for j in d[i]:
            cur[j] = 0
        sz = len(d[i])
        for idj in range(sz - 1, -1, -1):
            j = d[i][idj]
            uni[j] = add(sum_arr[j], sum_arr[j])
            for idk in range(idj + 1, sz):
                k = d[i][idk]
                if k % j != 0:
                    continue
                uni[j] = add(uni[j], -uni[k])
            cur[j] = add(uni[j], -add(dp[j], dp[j]))

        cur[i] += 1

        for j in d[i]:
            dp[j] = add(dp[j], cur[j])
            for k in d[j]:
                sum_arr[k] = add(sum_arr[k], cur[j])
            ans = add(ans, cur[j])

    print(ans)

def main():
    precompute()
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()