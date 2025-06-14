# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1214/problem/A

def alif():
    n = int(input())
    d = int(input())
    e = int(input())
    e *= 5
    result = n
    i = 0

    while i <= n:
        result = min(result, (n - i) % d)
        i += e
    print(result)

if __name__ == "__main__":
    alif()