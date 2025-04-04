# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    x, y, z = map(int, input().split())
    ans = 0

    while y > 0 and z > 1:
        ans += 3
        y -= 1
        z -= 2

    while x > 0 and y > 1:
        ans += 3
        x -= 1
        y -= 2

    print(ans)

t = int(input())
for _ in range(t):
    solve()