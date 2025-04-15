# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    f = [-float('inf')] * (m + 1)
    f[0] = 0
    s = 0
    d = [0] * (m + 2)

    for val in a:
        if val > 0:
            if val <= s:
                d[val] += 1
                if s + 1 <= m:
                    d[s + 1] -= 1
        elif val < 0:
            if 0 <= val + s:
                d[0] += 1
                if val + s + 1 <= m:
                    d[val + s + 1] -= 1
        else:
            s += 1
            for j in range(s + 1):
                if j > 0:
                    d[j] += d[j - 1]
                if j <= m:
                    f[j] += d[j]

            for j in range(s, 0, -1):
                if j <= m and j - 1 >= 0:
                    f[j] = max(f[j], f[j - 1])
            d = [0] * (m + 2)

    for i in range(m + 1):
        if i > 0:
            d[i] += d[i - 1]
        f[i] += d[i]

    print(max(f))

if __name__ == "__main__":
    solve()