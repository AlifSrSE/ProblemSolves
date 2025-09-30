# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
sys.setrecursionlimit(200000)

def dfs(node, g, pop, hap, vis, possible):
    if not possible[0]:
        return
    if vis[node]:
        return
    vis[node] = True
    cnt = 0
    
    for neighbor in g[node]:
        if not vis[neighbor]:
            dfs(neighbor, g, pop, hap, vis, possible)
            if not possible[0]:
                return
            pop[node] += pop[neighbor]
            cnt += hap[neighbor]

    if (hap[node] + pop[node]) % 2 != 0:
        possible[0] = False
        return
    p_plus = (hap[node] + pop[node]) // 2

    if p_plus < 0 or p_plus > pop[node]:
        possible[0] = False
        return

    if p_plus < cnt:
        possible[0] = False
        return
    hap[node] = p_plus


def alif():
    data = sys.stdin.read().split()
    
    if not data:
        return
    t = int(data[0])
    pointer = 1
    output = []

    for _ in range(t):
        n = int(data[pointer])
        m = int(data[pointer + 1])
        pointer += 2

        pop = [0] * (n + 1)
        for i in range(1, n + 1):
            pop[i] = int(data[pointer])
            pointer += 1

        hap = [0] * (n + 1)
        for i in range(1, n + 1):
            hap[i] = int(data[pointer])
            pointer += 1

        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(data[pointer])
            v = int(data[pointer + 1])
            pointer += 2
            g[u].append(v)
            g[v].append(u)

        vis = [False] * (n + 1)
        possible = [True]
        dfs(1, g, pop, hap, vis, possible)

        if possible[0]:
            output.append("YES")
        else:
            output.append("NO")

    sys.stdout.write('\n'.join(output) + '\n')

alif()
