# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1176/problem/A

def alif(n):
    exponent2 = 0
    while n % 2 == 0:
        exponent2 += 1
        n //= 2

    exponent3 = 0
    while n % 3 == 0:
        exponent3 += 1
        n //= 3

    exponent5 = 0
    while n % 5 == 0:
        exponent5 += 1
        n //= 5

    return exponent2 + exponent3 * 2 + exponent5 * 3 if n == 1 else -1

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(alif(n))
