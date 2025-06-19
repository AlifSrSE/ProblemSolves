# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1225/problem/C

def bitcount(x):
    count = 0
    if x < 0:
        return float('inf')
    return bin(x).count('1')

def alif():
    n, p = map(int, input().split())
    res = -1

    for a in range(1, 35):
        tmp = n - a * p
        if tmp >= a and bitcount(tmp) <= a:
            res = a
            break

    print(res)

if __name__ == "__main__":
    alif()