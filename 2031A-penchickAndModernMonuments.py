# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    f = [0] * n
    for x in map(int, input().split()):
        f[x-1] += 1
    print(n - max(f))

t = int(input())
for _ in range(t):
    solve()