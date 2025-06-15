# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1215/problem/D

def alif():
    n = int(input())
    s = input()
    diff = 0
    imb = 0

    for p in range(len(s)):
        sgn = -1 if (2 * p < n) else 1
        if s[p] == '?':
            imb += sgn
        else:
            diff += int(s[p]) * sgn

    if (2 * diff + 9 * imb) == 0:
        print("Bicarp")
    else:
        print("Monocarp")

if __name__ == "__main__":
    alif()