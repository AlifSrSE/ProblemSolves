# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def power(a, b, p):
    res = 1 % p
    while b > 0:
        if b & 1:
            res = (res * a) % p
        a = (a * a) % p
        b >>= 1
    return res

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 10**9 + 7

    for i in range(n):
        if a[i] == b[i] or b[i] == 0:
            print(1)
        else:
            print(power(2, b[i], mod))

if __name__ == "__main__":
    solve()