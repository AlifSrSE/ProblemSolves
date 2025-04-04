# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    cnt = ans // n
    if ans % n:
        cnt += 1
    print(cnt)

t = int(input())
for _ in range(t):
    solve()