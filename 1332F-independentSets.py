# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

MOD = 998244353

def read_ints():
    return map(int, sys.stdin.buffer.readline().split())

def alif():
    sys.setrecursionlimit(10**7)
    n = int(sys.stdin.buffer.readline())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = read_ints()
        u -= 1; v -= 1
        g[u].append(v)
        g[v].append(u)

    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = -2
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)

    order.reverse()

    A = [0] * n
    B = [0] * n
    C = [0] * n

    for u in order:
        prodC = 1
        prodCA = 1
        prodCAB = 1
        for v in g[u]:
            if v == parent[u]:
                continue
            cv = C[v]
            av = A[v]
            bv = B[v]
            prodC   = (prodC   * cv) % MOD
            prodCA  = (prodCA  * ((cv + av) % MOD)) % MOD
            prodCAB = (prodCAB * ((cv + av + bv) % MOD)) % MOD

        A[u] = prodCAB
        B[u] = prodCA
        C[u] = (prodCAB + prodCA - prodC) % MOD

    ans = (C[0] - 1) % MOD
    print(ans)

if __name__ == "__main__":
    alif()