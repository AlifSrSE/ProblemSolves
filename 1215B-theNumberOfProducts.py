# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1215/problem/B

def alif():
    n = int(input())
    arr = list(map(int, input().split()))
    fpos = 0
    fneg = 0
    spos = 0
    sneg = 0

    for x in arr:
        if x > 0:
            fpos += 1
        else:
            temp_fpos = fpos
            fpos = fneg
            fneg = temp_fpos + 1
        sneg += fneg
        spos += fpos

    print(sneg, spos)

if __name__ == "__main__":
    alif()