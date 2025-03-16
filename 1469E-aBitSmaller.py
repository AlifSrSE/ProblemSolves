# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1469/problem/E

def ceil_log(x):
    y = 0
    while (1 << y) < x:
        y += 1
    return y

def solve():
    n, k = map(int, input().split())
    t = input()

    m = min(k, ceil_log(n - k + 2))
    used = [0] * (1 << m)
    next0 = [int(1e9)] * n

    if t[n - 1] == '0':
        next0[n - 1] = n - 1
    for j in range(n - 2, -1, -1):
        if t[j] == '0':
            next0[j] = j
        else:
            next0[j] = next0[j + 1]

    d = k - m
    for j in range(n - k + 1):
        if next0[j] - j < d:
            continue
        cur = 0
        for x in range(j + d, j + k):
            cur = cur * 2 + (ord(t[x]) - ord('0'))
        used[((1 << m) - 1) ^ cur] = 1

    ans = -1
    for j in range(1 << m):
        if used[j] == 0:
            ans = j
            break

    if ans == -1:
        print("NO")
    else:
        print("YES")
        res = "0" * d
        res2 = ""
        for j in range(m):
            res2 += chr(ord('0') + (ans % 2))
            ans //= 2
        res2 = res2[::-1]
        res += res2
        print(res)

q = int(input())
for _ in range(q):
    solve()