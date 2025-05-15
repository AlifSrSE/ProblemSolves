# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1182/problem/A

def alif(n):
    return 1 << (n // 2) if n % 2 == 0 else 0

if __name__ == "__main__":
    n = int(input())
    print(alif(n))
