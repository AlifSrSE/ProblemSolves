# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1163/problem/A

def alif():
    n, m = map(int, input().split())
    if m < n - m:
        result = m if m > 0 else 1
    else:
        result = n - m
    print(result)

if __name__ == "__main__":
    alif()