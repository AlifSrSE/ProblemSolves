# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2122/problem/B

import sys

def alif():
    ni = int(sys.stdin.readline())
    ipi = []
    tri = []

    for _ in range(ni):
        i_xi, i_yi, t_xi, t_yi = map(int, sys.stdin.readline().split())
        ipi.append((i_xi, i_yi))
        tri.append((t_xi, t_yi))
    change = []

    for i in range(ni):
        change_xi = tri[i][0] - ipi[i][0]
        change_yi = tri[i][1] - ipi[i][1]
        change.append((change_xi, change_yi))
    ans = 0

    for i in range(ni):
        if change[i][1] < 0:
            ans += abs(change[i][1]) + (ipi[i][0] - abs(min(change[i][0], 0)))

        if change[i][0] < 0:
            ans += abs(change[i][0])
            
    sys.stdout.write(str(ans) + "\n")
numi_testi_casesi = int(sys.stdin.readline())

for _ in range(numi_testi_casesi):
    alif()