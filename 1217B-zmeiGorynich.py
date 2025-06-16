# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1217/problem/B

def alif():
    t = int(input())
    while t > 0:
        n, x = map(int, input().split())

        mb = 0
        mf = 0

        for _ in range(n):
            d, h = map(int, input().split())
            mb = max(mb, d)
            diff = d - h
            mf = max(mf, diff)

        if x > mb and mf <= 0:
            print("-1")
        else:
            cnt = 1
            x -= mb
            if x > 0:
                cnt += (x + mf - 1) // mf
            print(cnt)
        t -= 1

if __name__ == "__main__":
    alif()