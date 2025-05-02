# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1165/problem/A

def alif(digits, x, y):
    return sum(1 for i in range(x) if digits[-(i + 1)] != ('1' if i == y else '0'))

n, x, y = map(int, input().split())
digits = input()
print(alif(digits, x, y))