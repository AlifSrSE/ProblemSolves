# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1197/problem/C

def alif():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [a[p] - a[p - 1] for p in range(1, n)]
    b.sort(reverse=True)
    res = a[-1] - a[0]

    for p in range(k - 1):
        res -= b[p]
    
    print(res)

if __name__ == "__main__":
    alif()