# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    c = [0, 0]
    nums = list(map(int, input().split()))
    for x in nums:
        c[x & 1] += 1
    if c[0]:
        print(1 + c[1])
    else:
        print(c[1] - 1)

t = int(input())
for _ in range(t):
    solve()