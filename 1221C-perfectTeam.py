# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    x, y, z = map(int, input().split())
    cnt = min(x, y)
    if cnt <= z:
        ans = cnt
    else:
        ans = (x + y + z) // 3
        if ans > cnt:
            ans = cnt
    print(ans)

t = int(input())
for _ in range(t):
    solve()