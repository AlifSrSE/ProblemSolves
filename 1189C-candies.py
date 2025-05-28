# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1189/problem/C

def alif():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] * (n + 1)

    for p in range(1, n + 1):
        b[p] = b[p - 1] + a[p]
    
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        print((b[r] - b[l - 1]) // 10)

if __name__ == "__main__":
    alif()