# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
import bisect

input = sys.stdin.read
data = input().split()
idx = 0

n = int(data[idx]); idx += 1
q = int(data[idx]); idx += 1
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(data[idx]); idx += 1

queries = []
for i in range(q):
    x = int(data[idx]); idx += 1
    y = int(data[idx]); idx += 1
    queries.append((x, y, i))

queries.sort(key=lambda p: (n - p[1], p[0]))

bit = [0] * (n + 2)

def update(i, x):
    while i <= n + 1:
        bit[i] += x
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

ans = [0] * q
j = 1
for x, y, idx_ans in queries:
    L = x + 1
    R = n - y
    while j <= R:
        pos = j
        val = a[pos]
        if val <= pos:
            lo, hi = 1, pos + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if query(mid) >= pos - val:
                    hi = mid
                else:
                    lo = mid + 1
            update(1, 1)
            update(lo, -1)
        j += 1
    ans[idx_ans] = query(L)

print("\n".join(map(str, ans)))