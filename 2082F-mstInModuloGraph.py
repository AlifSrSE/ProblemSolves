# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    p = sorted(list(set(p)))
    n = len(p)
    maxN = p[-1] + 10

    class DSU:
        def __init__(self, n):
            self.cnt = n
            self.p = list(range(n))
            self.sz = [1] * n
            self.comp = [ [i] for i in range(n)]

        def find(self, v):
            if self.p[v] == v:
                return v
            self.p[v] = self.find(self.p[v])
            return self.p[v]

        def unite(self, u, v):
            u = self.find(u)
            v = self.find(v)
            if u == v:
                return False
            self.cnt -= 1
            if self.sz[u] > self.sz[v]:
                u, v = v, u
            for x in self.comp[u]:
                self.comp[v].append(x)
            self.comp[u] = []
            self.p[u] = v
            self.sz[v] += self.sz[u]
            return True

    T = DSU(n)
    res = 0

    while T.cnt > 1:
        minEdge = [float('inf')] * n
        to = [0] * n
        st = set((p[i], i) for i in range(n))

        for i in range(n):
            if T.p[i] != i:
                continue
            for ind in T.comp[i]:
                st.discard((p[ind], ind))
            for ind in T.comp[i]:
                for x in range(p[ind], maxN, p[ind]):
                    it = next((val for val in st if val[0] >= x), None)
                    if it:
                        w = it[0] - x
                        j = T.find(it[1])
                        if w < minEdge[i]:
                            minEdge[i] = w
                            to[i] = j
                        if w < minEdge[j]:
                            minEdge[j] = w
                            to[j] = i
            for ind in T.comp[i]:
                st.add((p[ind], ind))
        for i in range(n):
            if minEdge[i] != float('inf') and T.unite(i, to[i]):
                res += minEdge[i]
    print(res)

if __name__ == "__main__":
    _t = int(input())
    for _ in range(_t):
        solve()