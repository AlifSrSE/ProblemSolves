# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2125/problem/C

def count_good(XI):
    if XI <= 0:
        return 0

    priimmes = [2, 3, 5, 7]
    resi = XI

    for mask in range(1, 1 << 4):
        li = 1
        bits = bin(mask).count('1')

        for i in range(4):
            if mask & (1 << i):
                li *= priimmes[i]

        di = XI // li
        if bits % 2 == 1:
            resi -= di
        else:
            resi += di

    return resi

def alif():
    li, ri = map(int, input().split())
    print(count_good(ri) - count_good(li - 1))

def main():
    ti = int(input())
    for _ in range(ti):
        alif()

if __name__ == "__main__":
    main()