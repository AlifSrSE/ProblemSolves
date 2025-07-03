# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1245/problem/A

import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def alif():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        common_divisor = gcd(a, b)
        if common_divisor <= 1:
            print("Finite")
        else:
            print("Infinite")

if __name__ == "__main__":
    alif()