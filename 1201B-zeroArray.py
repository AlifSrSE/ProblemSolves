# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1201/problem/B

def alif():
    n = int(input())
    total = 0
    mx = 0

    for _ in range(n):
        x = int(input())
        total += x
        mx = max(mx, x)

    if (total % 2 != 0) or (2 * mx > total):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    alif()