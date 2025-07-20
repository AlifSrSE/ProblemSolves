# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1249/problem/B1

import sys

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        n = int(sys.stdin.readline())
        a = [0] + list(map(int, sys.stdin.readline().split()))
        b = [False] * (n + 1)
        dur = [0] * (n + 1)

        for p in range(1, n + 1):
            if b[p]:
                continue
            
            current_cycle_nodes = []
            cur = p

            while not b[cur]:
                b[cur] = True
                current_cycle_nodes.append(cur)
                cur = a[cur]

            cycle_length = len(current_cycle_nodes)
            for node_in_cycle in current_cycle_nodes:
                dur[node_in_cycle] = cycle_length
        
        sys.stdout.write(" ".join(map(str, dur[1:])) + "\n")

if __name__ == "__main__":
    alif()