# Author: AlifSrSE 
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/contest/1179/problem/A

def solve():
    n, q = map(int, input().split())
    v = list(map(int, input().split()))
    x = list(v)
    mx = 0
    mxid = -1
    ansmin = [(0, 0)] 

    for j in range(1, n + 1):
        a = x[0]
        b = x[1]
        x.pop(0)
        if a > b:
            x[0] = a
            x.append(b)
        else:
            x.append(a)
        ansmin.append((a, b))
        if j == n:
            v = list(x)

    for i in range(n):
        if v[i] > mx:
            mx = v[i]
            mxid = i

    if mxid != -1:
        v.pop(mxid)

    for _ in range(q):
        m = int(input())
        if m <= n:
            print(f"{ansmin[m][0]} {ansmin[m][1]}")
        else:
            if n > 1:
                m %= (n - 1)
                if m == 0:
                    m = n - 1
                m -= 2
                if m < 0:
                    m += (n - 1)
                print(f"{mx} {v[m]}")
            elif n == 1:
                print(f"{ansmin[1][0]} {ansmin[1][1]}")

if __name__ == "__main__":
    solve()