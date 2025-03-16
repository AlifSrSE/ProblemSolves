# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1896/problem/E

class BIT:
    def __init__(self, n):
        self.n = n
        self.v = [0] * (n + 1)

    def inc(self, pos, delta=1):
        i = pos
        while i <= self.n:
            self.v[i] += delta
            i += i & (-i)

    def dec(self, pos, delta=1):
        self.inc(pos, -delta)

    def qry(self, r):
        ret = 0
        i = r
        while i:
            ret += self.v[i]
            i &= i - 1
        return ret

    def range_qry(self, l, r):
        return self.qry(r) - self.qry(l - 1)

    def upd(self, pos, val):
        self.inc(pos, val - self.point_qry(pos))

    def point_qry(self, pos):
        return self.qry(pos) - self.qry(pos - 1)

def solve():
    n = int(input())
    end = BIT(2 * n)
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    a_input = list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = a_input[i - 1]
        if a[i] > i:
            b[i] = a[i]
            end.inc(b[i] + n)
        elif a[i] < i:
            b[i] = a[i] + n
        else:
            b[i] = a[i]
            end.inc(i)
            end.inc(n + i)
    for i in range(n, 0, -1):
        if i == b[i]:
            c[a[i]] = 0
            continue
        c[a[i]] = b[i] - i - end.range_qry(i, b[i])
        end.inc(b[i])
    print(*c[1:])

t = int(input())
for _ in range(t):
    solve()