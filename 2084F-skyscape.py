# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

from typing import List, Set, Tuple
import math

class FenwickTreeNode:
    def __init__(self, a: int = float('-inf')):
        self.a = a
    
    def __iadd__(self, other: 'FenwickTreeNode') -> 'FenwickTreeNode':
        self.a = max(self.a, other.a)
        return self
    
    def __lt__(self, other: 'FenwickTreeNode') -> bool:
        return self.a < other.a

class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.fenw = [FenwickTreeNode() for _ in range(n)]
        self.pw = 2 ** math.floor(math.log2(n if n > 0 else 1))
    
    def modify(self, x: int, v: FenwickTreeNode) -> None:
        assert 0 <= x <= self.n
        while x < self.n:
            self.fenw[x] += v
            x |= x + 1
    
    def query(self, x: int) -> FenwickTreeNode:
        assert 0 <= x <= self.n
        v = FenwickTreeNode()
        while x > 0:
            v += self.fenw[x - 1]
            x &= x - 1
        return v
    
    def max_prefix(self, c: FenwickTreeNode) -> int:
        v = FenwickTreeNode()
        at = 0
        len_val = self.pw
        while len_val > 0:
            if at + len_val <= self.n:
                nv = FenwickTreeNode(v.a)
                nv += self.fenw[at + len_val - 1]
                if not (c < nv):
                    v = nv
                    at += len_val
            len_val >>= 1
        assert 0 <= at <= self.n
        return at

def solve():
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    b = list(map(lambda x: int(x) - 1, input().split()))
    
    pos = [-1] * n
    for i in range(n):
        if b[i] != -1:
            pos[b[i]] = i
    
    l = [0] * n
    r = [n - 1] * n
    
    fenw = FenwickTree(n)
    for i in range(n):
        lim = fenw.query(a[i]).a
        l[a[i]] = max(l[a[i]], lim)
        if pos[a[i]] != -1:
            fenw.modify(a[i], FenwickTreeNode(pos[a[i]]))
    
    fenw = FenwickTree(n)
    for i in range(n - 1, -1, -1):
        lim = -fenw.query(n - 1 - a[i]).a
        r[a[i]] = min(r[a[i]], lim)
        if pos[a[i]] != -1:
            fenw.modify(n - 1 - a[i], FenwickTreeNode(-pos[a[i]]))
    
    at = [[] for _ in range(n)]
    for i in range(n):
        if pos[i] == -1:
            at[l[i]].append(i)
    
    ok = True
    for i in range(n):
        if l[i] > r[i]:
            ok = False
            break
        if pos[i] != -1:
            if l[i] > pos[i] or r[i] < pos[i]:
                ok = False
                break
    
    if not ok:
        print(-1)
        return
    
    s: Set[Tuple[int, int]] = set()
    for i in range(n):
        for j in at[i]:
            s.add((r[j], j))
        
        if b[i] == -1:
            if not s:
                ok = False
                break
            min_pair = min(s)
            if min_pair[0] < i:
                ok = False
                break
            b[i] = min_pair[1]
            s.remove(min_pair)
    
    if not ok:
        print(-1)
    else:
        print(' '.join(str(x + 1) for x in b))

def main():
    tt = int(input())
    for _ in range(tt):
        solve()

if __name__ == "__main__":
    main()