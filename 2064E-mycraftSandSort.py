# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys

def solve():
    MOD = 998244353
    
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        p = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
        c = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
        
        where = [0] * n
        color = [0] * n
        groups = [set() for _ in range(n)]
        
        top = 0
        i, j = 0, 0
        while i < n:
            while j < n and c[j] == c[i]:
                where[p[j]] = top
                j += 1
            color[top] = c[i]
            i = j
            top += 1
        
        for i in range(n):
            groups[where[i]].add(i)
        
        ans = 1
        alive = set(range(top))
        
        for i in range(n):
            at = where[i]
            ans = (ans * len(groups[at])) % MOD
            groups[at].remove(i)
            
            if not groups[at]:
                it = sorted(alive).index(at)
                if it > 0 and it < len(alive) - 1:
                    prev_it = sorted(alive)[it - 1]
                    next_it = sorted(alive)[it + 1]
                    if color[prev_it] == color[next_it]:
                        x, y = prev_it, next_it
                        alive.discard(x)
                        alive.discard(y)
                        alive.discard(at)
                        
                        if len(groups[x]) < len(groups[y]):
                            x, y = y, x
                        
                        groups[x].update(groups[y])
                        for z in groups[y]:
                            where[z] = x
                        groups[y].clear()
                        alive.add(x)
                    else:
                        alive.discard(at)
                else:
                    alive.discard(at)
        
        print(ans)

if __name__ == "__main__":
    solve()