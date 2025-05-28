# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1189/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if a[n - 1] >= a[n - 2] + a[n - 3]:
        print("NO")
    else:
        a[n - 2], a[n - 1] = a[n - 1], a[n - 2]
        print("YES")
        print(*a)

if __name__ == "__main__":
    alif()