# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1230/problem/A

def alif():
    a = list(map(int, input().split()))
    a.sort()
    possible = False

    if a[3] == a[0] + a[1] + a[2]:
        possible = True
    elif a[0] + a[3] == a[1] + a[2]:
        possible = True
    if possible:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    alif()