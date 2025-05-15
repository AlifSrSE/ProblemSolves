# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1178/problem/C

MODULUS = 998244353

def alif(w, h):
    return pow(2, w + h, MODULUS)

if __name__ == "__main__":
    w = int(input())
    h = int(input())
    print(alif(w, h))
