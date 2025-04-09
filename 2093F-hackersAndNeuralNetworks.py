# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = input().split()
        can = [False] * n
        mf = 0

        for _ in range(m):
            b = input().split()
            cnt = 0
            for j in range(n):
                if b[j] == a[j]:
                    cnt += 1
                    can[j] = True
            mf = max(mf, cnt)

        if all(can):
            print(3 * n - 2 * mf)
        else:
            print(-1)
solve()
