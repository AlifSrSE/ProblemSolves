# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1469/problem/F

import sys

class Node:
    def __init__(self):
        self.mn = float('inf')
        self.mx = float('-inf')
        self.val = 0

class SegTree:
    def __init__(self):
        self.N = 0
        self.st = []
        self.cLazy = []
        self.lazy = []

    def init(self, n):
        self.N = n
        self.st = [Node() for _ in range(4 * self.N + 5)]
        self.cLazy = [False] * (4 * self.N + 5)
        self.lazy = [0] * (4 * self.N + 5)

    def merge(self, cur, l, r):
        cur.mn = min(l.mn, r.mn)
        cur.mx = max(l.mx, r.mx)
        cur.val = l.val + r.val

    def propagate(self, ver, L, R):
        if L != R:
            self.cLazy[ver * 2] = self.cLazy[ver * 2 + 1] = True
            self.lazy[ver * 2] += self.lazy[ver]
            self.lazy[ver * 2 + 1] += self.lazy[ver]
        self.st[ver].val += (R - L + 1) * self.lazy[ver]
        self.cLazy[ver] = self.lazy[ver] = 0

    def build(self, ver, L, R, a):
        if L > R:
            return
        if L == R:
            self.st[ver].mn = a[L - 1]
            self.st[ver].mx = a[L - 1]
            self.st[ver].val = a[L - 1]
            return
        M = (L + R) // 2
        self.build(ver * 2, L, M, a)
        self.build(ver * 2 + 1, M + 1, R, a)
        self.merge(self.st[ver], self.st[ver * 2], self.st[ver * 2 + 1])

    def query(self, ver, L, R, i, j):
        if self.cLazy[ver]:
            self.propagate(ver, L, R)
        if j < L or i > R:
            return Node()
        if i <= L and R <= j:
            return self.st[ver]
        M = (L + R) // 2
        left = self.query(ver * 2, L, M, i, j)
        right = self.query(ver * 2 + 1, M + 1, R, i, j)
        cur = Node()
        self.merge(cur, left, right)
        return cur

    def pquery(self, ver, L, R, pos):
        if self.cLazy[ver]:
            self.propagate(ver, L, R)
        if L == R:
            return self.st[ver]
        M = (L + R) // 2
        if pos <= M:
            return self.pquery(ver * 2, L, M, pos)
        else:
            return self.pquery(ver * 2 + 1, M + 1, R, pos)

    def update(self, ver, L, R, i, j, val):
        if self.cLazy[ver]:
            self.propagate(ver, L, R)
        if j < L or i > R:
            return
        if i <= L and R <= j:
            self.cLazy[ver] = True
            self.lazy[ver] += val
            self.propagate(ver, L, R)
            return
        M = (L + R) // 2
        self.update(ver * 2, L, M, i, j, val)
        self.update(ver * 2 + 1, M + 1, R, i, j, val)
        self.merge(self.st[ver], self.st[ver * 2], self.st[ver * 2 + 1])

    def pupdate(self, ver, L, R, pos, val):
        if self.cLazy[ver]:
            self.propagate(ver, L, R)
        if L == R:
            self.st[ver].mn += val
            self.st[ver].mx += val
            self.st[ver].val += val
            return
        M = (L + R) // 2
        if pos <= M:
            self.pupdate(ver * 2, L, M, pos, val)
        else:
            self.pupdate(ver * 2 + 1, M + 1, R, pos, val)
        self.merge(self.st[ver], self.st[ver * 2], self.st[ver * 2 + 1])

    def get(self, x):
        v = 1
        lv = 1
        rv = self.N
        if self.cLazy[v]:
            self.propagate(v, lv, rv)
        if self.st[v].val < x:
            return -1
        sum_val = 0
        while lv != rv:
            mid = (lv + rv) // 2
            if self.cLazy[v * 2]:
                self.propagate(v * 2, lv, mid)
            if self.st[v * 2].val + sum_val >= x:
                rv = mid
                v = v * 2
            else:
                sum_val += self.st[v * 2].val
                if self.cLazy[v * 2 + 1]:
                    self.propagate(v * 2 + 1, mid + 1, rv)
                lv = mid + 1
                v = v * 2 + 1
        return lv

    def query_pos(self, pos):
        return self.pquery(1, 1, self.N, pos)

    def query_range(self, l, r):
        return self.query(1, 1, self.N, l, r)

    def update_pos(self, pos, val):
        self.pupdate(1, 1, self.N, pos, val)

    def update_range(self, l, r, val):
        self.update(1, 1, self.N, l, r, val)

    def show(self, n):
        for i in range(1, n + 1):
            sys.stderr.write(str(self.query_pos(i).val) + " ")
        sys.stderr.write("\n")

def ceil_div(x, y):
    return (x + y - 1) // y

n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
i = 0
ans = 10**9
MAXD = 10**5 + 1000
rq = SegTree()
rq.init(MAXD)

for d in range(MAXD):
    if d:
        x = rq.query_pos(d).val
    else:
        x = 1
    j = 1
    while i < n and j <= x:
        if d:
            rq.update_pos(d, -1)
        l[i] -= 1
        rq.update_range(d + 2, min(d + 1 + l[i] // 2, MAXD - 1), 1)
        rq.update_range(d + 2, min(MAXD - 1, d + 1 + ceil_div(l[i], 2)), 1)
        best = rq.get(k)
        if best != -1:
            ans = min(ans, best)
        i += 1
        j += 1
    if d:
        rq.update_pos(d, -rq.query_pos(d).val)

print(ans if ans < 10**9 else -1)