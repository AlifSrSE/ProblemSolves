# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2070/problem/E

class Segtree:
    def __init__(self):
        self.T = [0] * (4 * 4 * 300003)

    def add(self, v, l, r, pos, val):
        self.T[v] += val
        if l != r - 1:
            m = (l + r) // 2
            if pos < m:
                self.add(v * 2 + 1, l, m, pos, val)
            else:
                self.add(v * 2 + 2, m, r, pos, val)

    def get(self, v, l, r, L, R):
        if L >= R:
            return 0
        if l == L and r == R:
            return self.T[v]
        m = (l + r) // 2
        return self.get(v * 2 + 1, l, m, L, min(m, R)) + self.get(v * 2 + 2, m, r, max(m, L), R)

    def getSumLess(self, l):
        return self.get(0, 0, 4 * 300003, 0, l + 3 * 300003)

    def add_val(self, pos, val):
        self.add(0, 0, 4 * 300003, pos + 3 * 300003, val)

threshold = [0, 1, 1, -2]

def solve():
    n = int(input())
    s = input()
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + (-3 if s[i] == '1' else 1)
    
    trees = [Segtree() for _ in range(4)]
    ans = 0
    for i in range(n + 1):
        for j in range(4):
            length = (i - j + 4) % 4
            bound = p[i] - threshold[length]
            ans += trees[j].getSumLess(bound)
        trees[i % 4].add_val(p[i], 1)
    
    print(ans)

solve()