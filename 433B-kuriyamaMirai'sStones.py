# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)

    for i in range(1, n):
        a[i] += a[i - 1]
        b[i] += b[i - 1]

    m = int(input())
    for _ in range(m):
        x, l, r = map(int, input().split())
        if x == 1:
            if l == 1:
                print(a[r - 1])
            else:
                print(a[r - 1] - a[l - 2])
        else:
            if l == 1:
                print(b[r - 1])
            else:
                print(b[r - 1] - b[l - 2])

if __name__ == "__main__":
    solve()